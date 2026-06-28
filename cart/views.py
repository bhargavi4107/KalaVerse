from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Cart
from store.models import Product


@login_required
def add_to_cart(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("cart")


@login_required
def cart_view(request):

    cart_items = Cart.objects.filter(user=request.user)

    grand_total = 0

    for item in cart_items:
        grand_total += item.product.price * item.quantity

    return render(
        request,
        "cart/cart.html",
        {
            "cart_items": cart_items,
            "grand_total": grand_total
        }
    )

@login_required
def remove_from_cart(request, cart_id):

    cart_item = get_object_or_404(
        Cart,
        id=cart_id,
        user=request.user
    )

    cart_item.delete()

    return redirect("cart")
