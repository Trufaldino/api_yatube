from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from .views import CommentViewSet, GroupViewSet, PostViewSet

router_v1 = routers.DefaultRouter()
router_v1.register(r'v1/posts', PostViewSet)
router_v1.register(r'v1/groups', GroupViewSet)
router_v1.register(r'v1/posts/(?P<post_id>[\d]+)/comments', CommentViewSet,
                   basename='comments')

urlpatterns = [
    path('', include(router_v1.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
