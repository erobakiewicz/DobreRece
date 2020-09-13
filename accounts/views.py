from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group, User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, DetailView

from accounts.forms import RegistrationForm


class UserCreateView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, "register.html", {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Donor')
            user.groups.add(group)
        else:
            form = RegistrationForm(request.POST)
            args = {'form': form}
            return render(request, "register.html", args)
        return redirect(reverse("login"))


class LoginPageView(LoginView):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse("index"))
        else:
            return redirect(reverse("register"))


class LogoutPageView(LogoutView):
    def get(self, request):
        return redirect(reverse("index"))

    def post(self, request):
        logout(request)


class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "user-profile.html"

    def get_object(self):
        return self.request.user
