from django.shortcuts import render, redirect
from .forms import LoginForm, UserRegisterForm
from django.views.generic import FormView, CreateView
from django.contrib.auth  import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse_lazy


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