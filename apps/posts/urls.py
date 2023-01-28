from django.urls import path
from apps.posts.views import (
    IndexPage, UserPostsView, PostCreateView, PostDetailView,
    archivate_post, unarchivate_post
)

urlpatterns = [
    path("", IndexPage.as_view(), name="index"),
    path("user_posts/", UserPostsView.as_view(), name="user_posts"),
    path("create_post/", PostCreateView.as_view(), name="create_post"),
    path("post/detail/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/archivate/<int:pk>/", archivate_post, name="archivate_post"),
    path("post/unarchivate/<int:pk>/", unarchivate_post, name="unarchivate_post"),
]