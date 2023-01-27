from django.urls import path
from .views import  RegisterView, LoginView, logout_user, UpdateUserView

urlpatterns = [
    path("login/", LoginView.as_view(), name="sign_in"),
    path("registration/", RegisterView.as_view(), name="register"),
    path("logout/", logout_user, name="logout"),
    path("user_profile/", UpdateUserView.as_view(), name="user_profile"),
]