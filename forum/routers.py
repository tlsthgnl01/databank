from rest_framework_nested import routers as nested_routers

from forum import views

forum_router = nested_routers.SimpleRouter(trailing_slash=False)
forum_router.register('posts', views.PostViewSet, basename='posts')
forum_comment_router = nested_routers.NestedSimpleRouter(forum_router, 'posts', lookup='post')  # forum/:{lookup}_pk
forum_comment_router.register('comments', views.CommentViewSet, basename='comments')
