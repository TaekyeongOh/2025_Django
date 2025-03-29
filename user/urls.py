from django.urls import path, include
from django.contrib import admin
from .views import signup_view, home

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', home, name="home"),

]