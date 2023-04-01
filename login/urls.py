from django.urls import path

from login.views import add_login

urlpatterns = [
    path('login/', add_login, name='add_login'),
]