from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here


from apps.posts.models import Post
from .forms import PostCreateForm, PostUpdateForm


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
        posts = Post.objects.filter(author=self.request.user)
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


class PostDetailView(DetailView):
    template_name = "post_details.html"
    model = Post
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = PostUpdateForm(instance=self.get_object())
        return context


def archivate_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if not post.is_archive:
        post.is_archive = True
    else:
        post.is_archive = False
    post.save()
    return redirect("user_posts")


# def unarchivate_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if post.is_archive:
#         post.is_archive = False
#         post.save()
#     return redirect("user_posts")


def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect("user_posts")


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostUpdateForm
    # success_url = reverse_lazy("user_posts")

    def get_success_url(self):
        pk = self.kwargs.get("pk")
        return reverse_lazy("post_detail", kwargs={"pk":pk})


class FollowinPostsView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "following_posts.html"

    def get_queryset(self):
        # наші підписки
        following = self.request.user.following.all()
        posts = Post.objects.filter(
            author__in=following,
            is_archive=False
        )
        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = PostCreateForm()
        return context