from django.urls import path
from apps.posts.views import IndexPage

urlpatterns = [
    path("", IndexPage.as_view(), name="index"),
]