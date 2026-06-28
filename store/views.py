from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Product, Order
from cart.models import Cart


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


@login_required
def checkout(request):

    cart_items = Cart.objects.filter(user=request.user)

    total = 0

    for item in cart_items:
        total += item.product.price * item.quantity

    if request.method == "POST":

        # Prevent placing an empty order
        if not cart_items.exists():
            return redirect("cart")

        Order.objects.create(
            user=request.user,
            total_amount=total
        )

        # Clear the cart after placing the order
        cart_items.delete()

        return redirect("orders")

    return render(
        request,
        "checkout.html",
        {
            "cart_items": cart_items,
            "total": total
        }
    )


@login_required
def orders(request):

    user_orders = Order.objects.filter(user=request.user)

    return render(
        request,
        "orders.html",
        {
            "orders": user_orders
        }
    )