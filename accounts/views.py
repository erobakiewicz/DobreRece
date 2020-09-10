from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

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
            form = RegistrationForm()
            args = {'form': form}
            return render(request, "register.html", args)
        return redirect(reverse("login"))