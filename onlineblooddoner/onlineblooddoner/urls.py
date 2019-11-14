"""onlineblooddoner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.views.generic import TemplateView

from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name="index.html")),
    path('home/',TemplateView.as_view(template_name="index.html"),name="home"),
    path('adminlogin/', TemplateView.as_view(template_name="adminlogin.html"),name="adminlogin"),
    path('donorlogin/',TemplateView.as_view(template_name="donorlogin.html"),name="donorlogin"),
    path('userlogin/', TemplateView.as_view(template_name="userlogin.html"), name="userlogin"),
    path('donorreg/',TemplateView.as_view(template_name="donoerregistration.html"),name="donorreg"),
    path('dregcancel/',TemplateView.as_view(template_name="index.html"),name="dregcancel"),
    path('userreg/', TemplateView.as_view(template_name="userregistration.html"), name="userreg"),
    path('uregcancel/', TemplateView.as_view(template_name="index.html"), name="uregcancel"),
    path('saveuser/',views.SaveUser.as_view(),name="saveuser"),
    path('savedoner/',views.SaveDonor.as_view(),name="savedoner"),
    path('donorloginchek/',views.DonorLoginchek.as_view(),name="donorloginchek"),
    path('userloginchek/',views.UserLoginchek.as_view(),name="userloginchek"),

]
