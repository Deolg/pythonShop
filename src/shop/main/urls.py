"""
Main module urls
"""
from django.urls import path
from . import views

# pylint: disable=invalid-name
app_name = 'main'

# pylint: disable=invalid-name
urlpatterns = [
    path('', views.ProductList, name='ProductList'),
    path('<str:slug>/', views.ProductList, name='ProductList'),
    path('detail/<int:pk>/', views.ProductDetail, name='ProductDetail'),
]
