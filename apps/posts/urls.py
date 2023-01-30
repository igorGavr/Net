from django.urls import path
from apps.posts.views import (
    IndexPage, UserPostsView, PostCreateView, PostDetailView,
    archivate_post, delete_post,
    PostUpdateView, FollowinPostsView, like_post, unlike_post
)

urlpatterns = [
    path("", FollowinPostsView.as_view(), name="index"),
    path("user_posts/", UserPostsView.as_view(), name="user_posts"),
    path("create_post/", PostCreateView.as_view(), name="create_post"),
    path("post/detail/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/archivate/<int:pk>/", archivate_post, name="archivate_post"),
    # path("post/unarchivate/<int:pk>/", unarchivate_post, name="unarchivate_post"),
    path("post/delete/<int:pk>/", delete_post, name="delete_post"),
    path("post/update/<int:pk>/", PostUpdateView.as_view(), name="update_post"),

    path("post/like/<int:post_pk>/", like_post, name="like_post"),
    path("post/unlike/<int:post_pk>/", unlike_post, name="unlike_post"),
]
