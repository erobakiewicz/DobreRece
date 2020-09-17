from django.urls import path
from django.contrib.auth import views as auth_views

from accounts import views
from accounts.views import UserCreateView, LoginPageView, UserProfileView, LogoutPageView, UpdateUserView

urlpatterns = [
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', LogoutPageView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('userprofile/', UserProfileView.as_view(), name='userprofile'),
    path('editprofile/<int:pk>', UpdateUserView.as_view(), name='editprofile'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path("password_reset/", views.password_reset_request, name="password_reset"),
]
