from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, UserRegisterForm, UserUpdateForm, UserPasswordChangeForm
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
    template_name = "user_profile_detail.html"
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


@login_required
def change_password(request):
    if request.method == "POST":
        form = UserPasswordChangeForm(request.user, request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            logout(request)
            return redirect("sign_in")
        return render(request, "password_change.html", {"form": form})
    else:
        form = UserPasswordChangeForm(request.user)
        context = {
            "form": form
        }
        return render(request, "password_change.html", context)




from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings


def password_reset_request(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            user = User.objects.get(email=email)
            subject = "Восстановления пароля."
            email_template_name = "password_reset_email.html"
            reset_data = {
                "email": user.email,
                # наш хост
                "domain": "127.0.0.1:8000",
                "site_name": "Website",
                # кодуємо айдішку
                "uid": urlsafe_base64_encode(force_bytes(user.id)),
                "user": user,
                # генеруємо токен
                "token": default_token_generator.make_token(user),
                "protocol": "http",
            }
            email = render_to_string(email_template_name, reset_data)
            print(email)
            try:
                send_mail(
                    subject=subject,
                    message=email,
                    recipient_list=[user.email],
                    from_email=settings.EMAIL_HOST_USER,
                    fail_silently=True,

                )
            except BadHeaderError:
                return HttpResponse("Invalid Header")
            return redirect(reverse_lazy("password_reset_done"))
    else:
        form = PasswordResetForm()
    return render(request, "password_reset.html", {"form": form})
