"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('store.urls')),

    path('', include('users.urls')),

    path('', include('cart.urls')),
]