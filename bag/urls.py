from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.bag, name='bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
]
