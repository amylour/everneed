from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('create', views.add_article, name='add_article'),
    path('<slug:slug>/', views.article, name='article'),
    path('edit/<slug:slug>/', views.edit_article, name='edit_article'),
]
