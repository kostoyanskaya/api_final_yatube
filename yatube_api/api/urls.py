from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_v1 = DefaultRouter()
router_v1.register(r'v1/posts', PostViewSet)
router_v1.register(r'v1/groups', GroupViewSet)
router_v1.register(r'v1/follow', FollowViewSet, basename='follow')
router_v1.register(
    r'v1/posts/(?P<post_id>[^/.]+)/comments',
    CommentViewSet, basename='comments'
)
urlpatterns = [
    path('', include(router_v1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
