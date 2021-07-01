from django.urls import include, path

from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    CommentViewSet,
    FollowViewSet,
    GroupListViewSet,
    PostViewSet
)

v1_router = routers.DefaultRouter()
v1_router.register('posts', PostViewSet, basename='post')
v1_router.register('group', GroupListViewSet, basename='group')
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet, basename='comment'
)
v1_router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('api/v1/', include(v1_router.urls)),
    path('api/v1/token/',
         TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/v1/token/refresh/',
         TokenRefreshView.as_view(),
         name='token_refresh'),
]
