from django.urls import path
from .views import  (
    RegisterView, LoginView, logout_user, UpdateUserView,
    UsersSearchListView, UserProfileView, FollowUser,
    UnfollowUser
)
urlpatterns = [
    path("login/", LoginView.as_view(), name="sign_in"),
    path("registration/", RegisterView.as_view(), name="register"),
    path("logout/", logout_user, name="logout"),
    path("user_profile/", UpdateUserView.as_view(), name="user_profile"),
    path("search/", UsersSearchListView.as_view(), name="search_users"),
    path("user/profile/detail/<int:pk>/", UserProfileView.as_view(), name="user_details"),

    path("follow/<int:user_pk>/", FollowUser.as_view(), name="follow"),
    path("unfollow/<int:user_pk>/", UnfollowUser.as_view(), name="unfollow"),
]