from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, CreateView

# Create your views here
from apps.posts.models import Post
from .forms import PostCreateForm


class IndexPage(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex["posts"] = Post.objects.all()
        return contex


class UserPostsView(ListView):
    template_name = "user_posts.html"
    model = Post

    def get_queryset(self):
        posts = Post.objects.filter(is_archive=False, author=self.request.user)
        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = PostCreateForm()
        return context


class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy("user_posts")

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)

