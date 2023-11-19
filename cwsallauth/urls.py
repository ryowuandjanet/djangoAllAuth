from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include

def home(request):
  return render(request, "home.html")

urlpatterns = [
  path('',home),
  path('admin/', admin.site.urls),
  path('accounts/', include('allauth.urls')),
]
