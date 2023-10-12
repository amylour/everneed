from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('admin_articles/',
         views.admin_article_list, name='admin_article_list'),
    path('add_article/', views.add_article, name='add_article'),
    path('edit/<slug:slug>/', views.edit_article, name='edit_article'),
    path('<slug:slug>/', views.article, name='article'),
    path('article/delete/<slug:slug>/',
         views.delete_article, name='delete_article'),
]
