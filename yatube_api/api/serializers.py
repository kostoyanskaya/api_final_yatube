from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Follow, Group, Post, User, Comment


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post', 'author')


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field='username'
    )

    class Meta:
        model = Follow
        fields = '__all__'

    def validate(self, data):
        user = self.context['request'].user
        following_user = data.get('following')

        if following_user == user:
            raise serializers.ValidationError('Нельзя подписаться на себя.')

        if Follow.objects.filter(user=user, following=following_user).exists():
            raise serializers.ValidationError('Уже подписаны на этого автора.')

        return data
