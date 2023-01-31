from django.urls import path
from .views import  (
    RegisterView, LoginView, logout_user, UpdateUserView,
    UsersSearchListView, UserProfileView, FollowUser,
    UnfollowUser, change_password, password_reset_request,

)

from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login/", LoginView.as_view(), name="sign_in"),
    path("registration/", RegisterView.as_view(), name="register"),
    path("logout/", logout_user, name="logout"),


    path("change_password/", change_password, name="change_password"),
    # коли забули пароль
    path("user/password/reset/", password_reset_request, name="password_reset"),
    #
    path("password_reset/done/",
         auth_views.PasswordResetDoneView.as_view(
             template_name="password_reset_done.html"),
         name="password_reset_done"),
    #
    path("reset/<uidb64>/<token>/",
         auth_views.PasswordResetConfirmView.as_view(
             template_name="password_reset_confirm.html"),
         name="password_reset_confirm"),
    #
    path("reset/done/",
         auth_views.PasswordResetCompleteView.as_view(
             template_name="password_reset_complete.html"),
         name="password_reset_complete"
         ),


    path("search/", UsersSearchListView.as_view(), name="search_users"),
    path("user_profile/", UpdateUserView.as_view(), name="user_profile"),
    path("user/profile/detail/<int:pk>/", UserProfileView.as_view(), name="user_details"),

    path("follow/<int:user_pk>/", FollowUser.as_view(), name="follow"),
    path("unfollow/<int:user_pk>/", UnfollowUser.as_view(), name="unfollow"),
]