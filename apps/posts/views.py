from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here
from apps.posts.models import Post


class IndexPage(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex["posts"] = Post.objects.all()
        return contex

