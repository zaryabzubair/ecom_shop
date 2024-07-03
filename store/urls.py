from django.urls import path
from . import views
urlpatterns = [
    path('', views.ProductList, name='product_list'),
    path('add/', views.AddProduct, name='add_product'),
]