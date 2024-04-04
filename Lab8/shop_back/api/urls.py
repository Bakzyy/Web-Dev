from django.urls import path, re_path
from api import views

urlpatterns = [
    path('categories/', views.categories),
    path('products/', views.products),
    path('categories/<int:id>/', views.get_category),
    path('products/<int:id>/', views.get_product),
    path('categories/<int:id>/products', views.get_products_by_category)
]