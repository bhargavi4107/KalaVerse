from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    products = Product.objects.all()

    context = {
        "products": products
    }

    return render(request, "home.html", context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    context = {
        "product": product
    }

    return render(request, "product_detail.html", context)
