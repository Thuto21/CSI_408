from django.contrib import admin
from django.urls import path

from registration.views import add_staff

urlpatterns = [
    path('register/', add_staff, name='add_staff'),
]