from .models import Product, Category
from django.shortcuts import get_object_or_404, render

# Create your views here.


def product_detail(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug)

    context =  {
        'product': product
    }

    return render(request, 'product_detail.html', context)

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all() 

    context =  {
        'category': category,
        'product': products
    }

    return render(request, 'category_detail.html', context)