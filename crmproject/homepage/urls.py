from django.urls import path


from . import views
from .views import crm_home

urlpatterns=[
    path('', views.crm_home, name='crm_home'),
    path('homepage/', views.crm_home, name='crm_home'),

]