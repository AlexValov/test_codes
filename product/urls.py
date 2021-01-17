from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('product/<slug>', views.product_detail, name='product_detail'),
]
