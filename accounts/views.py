from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group, User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail, BadHeaderError
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views import View
from django.views.generic import DetailView, UpdateView

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


class UpdateUserView(LoginRequiredMixin, UpdateView):
    template_name = 'EditUser.html'
    success_url = reverse_lazy("userprofile")
    model = User
    fields = ["first_name", "last_name", "email"]


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "registration/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect(reverse("password_reset_done"))
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="registration/password_reset_form.html",
                  context={"password_reset_form": password_reset_form})
