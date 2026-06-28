from django.urls import path
from . import views

urlpatterns = [
    path("add/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("artbag/", views.cart_view, name="cart"),
    path("remove/<int:cart_id>/", views.remove_from_cart, name="remove_from_cart"),
]