from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import UserCreateView, LoginPageView, UserProfileView, LogoutPageView, UpdateUserView

urlpatterns = [
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', LogoutPageView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('userprofile/', UserProfileView.as_view(), name='userprofile'),
    path('editprofile/<int:pk>', UpdateUserView.as_view(), name='editprofile'),


]
