from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('admin_product_list/', views.admin_product_list,
         name='admin_product_list'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('admin_product_detail/<int:product_id>/',
         views.admin_product_detail, name='admin_product_detail'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product,
         name='delete_product'),
]
