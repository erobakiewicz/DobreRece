from django.urls import path
from django.views.generic import TemplateView

from accounts.views import UserCreateView

urlpatterns = [
    path('login/', TemplateView.as_view(template_name="login.html"), name='login'),
    path('register/', UserCreateView.as_view(), name='register'),
]