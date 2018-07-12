"""
Main module urls
"""
from django.urls import path
from . import views

# pylint: disable=invalid-name
app_name = 'cart'

# pylint: disable=invalid-name
urlpatterns = [
    path('remove/<int:product_id>/', views.CartRemove, name='CartRemove'),
    path('add/<int:product_id>/', views.CartAdd, name='CartAdd'),
    path('', views.CartDetail, name='CartDetail')
]
