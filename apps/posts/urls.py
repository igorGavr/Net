from django.urls import path
from apps.posts.views import IndexPage, UserPostsView, PostCreateView

urlpatterns = [
    path("", IndexPage.as_view(), name="index"),
    path("user_posts/", UserPostsView.as_view(), name="user_posts"),
    path("create_post/", PostCreateView.as_view(), name="create_post"),
]