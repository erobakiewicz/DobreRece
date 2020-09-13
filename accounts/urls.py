from django.urls import path

from accounts.views import UserCreateView, LoginPageView, UserProfileView, LogoutPageView

urlpatterns = [
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', LogoutPageView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('userprofile/', UserProfileView.as_view(), name='userprofile'),

]
