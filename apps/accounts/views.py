from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, UserRegisterForm, UserUpdateForm
from django.views.generic import FormView, CreateView, UpdateView, ListView, DetailView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import User
from django.contrib import messages


class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm

    def form_valid(self, form):
        data = form.cleaned_data
        username = data["username"]
        password = data["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect("index")
            return HttpResponse("is not activa")
        return HttpResponse("Invalid user data")


class RegisterView(CreateView):
    template_name = "register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("index")


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("index")


class UpdateUserView(UpdateView):
    template_name = "profile.html"
    form_class = UserUpdateForm
    success_url = reverse_lazy("index")

    def get_object(self):
        return self.request.user


class UsersSearchListView(ListView):
    template_name = "users.html"
    model = User

    def get_queryset(self):
        search_text = self.request.GET.get("query")
        if search_text:
            search_users = User.objects.filter(username__icontains=search_text)
            return search_users
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_text"] = self.request.GET.get("query")
        return context


class UserProfileView(LoginRequiredMixin, DetailView):
    template_name = "user_profile.html"
    model = User
    queryset = User.objects.all()


class FollowUser(LoginRequiredMixin, View):

    def get(self, request, user_pk):
        from_user = request.user
        to_user = get_object_or_404(User, pk=user_pk)
        if from_user not in to_user.followers.all():
            messages.add_message(request, messages.SUCCESS, "вы успешно подписались")
            to_user.followers.add(from_user)
        return redirect("index")


class UnfollowUser(LoginRequiredMixin, View):

    def get(self, request, user_pk):
        from_user = request.user
        to_user = get_object_or_404(User, pk=user_pk)
        if from_user in to_user.followers.all():
            messages.add_message(request, messages.SUCCESS, "вы успешно отписались")
            to_user.followers.remove(from_user)
        return redirect("index")
