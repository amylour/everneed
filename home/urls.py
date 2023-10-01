from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact_form, name='contact_form'),
    path('thank-you/', views.thank_you, name='thank_you'),
]
