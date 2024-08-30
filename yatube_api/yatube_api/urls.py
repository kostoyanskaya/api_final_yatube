from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from api.views import PostViewSet, CommentViewSet, FollowViewSet, GroupViewSet


router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'follow', FollowViewSet, basename='subscription')

comment_router = DefaultRouter()
comment_router.register(
    r'posts/(?P<post_id>[^/.]+)/comments', CommentViewSet, basename='comments'
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include(comment_router.urls)),
    path('api/v1/', include('djoser.urls.jwt')),
]
