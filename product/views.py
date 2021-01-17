from django.shortcuts import render
from product.models import *
from home_page.models import *
from django.shortcuts import get_object_or_404

# Create your views here.

def home_page(request):
    product_list = Product.objects.all()
    home_page_data = HomePage.objects.all().last()
    return render (request, 'product/index.html', {
        'product_list' : product_list,
        'home_page_data' : home_page_data,
    })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)

    return render (request, 'product/product.html', {
        'product' : product
    })