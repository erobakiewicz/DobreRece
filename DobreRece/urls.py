"""DobreRece URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from charity import views
from charity.views import CategoryCreateView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.LandingPageView.as_view(template_name='index.html'), name='index'),
    path('category/create/', CategoryCreateView.as_view(), name="create_category"),

    path('form/', TemplateView.as_view(template_name='form.html'), name='form'),

    path("accounts/", include("accounts.urls")),

]
