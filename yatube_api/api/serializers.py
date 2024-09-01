from rest_framework import serializers

from posts.models import Follow, Group, Post, User, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )

    class Meta:
        model = Post
        fields = '__all__'


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
        read_only_fields = ('post',)


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

    def validate_following(self, value):
        user = self.context['request'].user
        if value == user:
            raise serializers.ValidationError('Нельзя подписаться на себя.')

        if Follow.objects.filter(user=user, following=value).exists():
            raise serializers.ValidationError('Уже подписаны на этого автора.')

        return value
