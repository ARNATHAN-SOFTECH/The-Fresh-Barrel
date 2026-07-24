from django.shortcuts import render, redirect
from products.models import Product
from .models import ShippingAddress
from datetime import date, timedelta
from decimal import Decimal

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from products.models import Product
from accounts.models import Address


@login_required
def checkout(request):

    cart = request.session.get("cart", {})

    cart_items = []
    total = 0

    for product_id, quantity in cart.items():

        try:
            product = Product.objects.get(id=product_id)

            subtotal = product.selling_price * quantity

            total += subtotal

            cart_items.append({
                "product": product,
                "quantity": quantity,
                "subtotal": subtotal,
            })

        except Product.DoesNotExist:
            continue

    # Get the default address
    default_address = Address.objects.filter(
        user=request.user,
        is_default=True
    ).first()

    if request.method == "POST":

        if not default_address:
            return render(
                request,
                "orders/checkout.html",
                {
                    "cart_items": cart_items,
                    "total": total,
                    "default_address": default_address,
                    "error": "Please add your delivery address."
                }
            )

        # Store selected address for the order
        request.session["address_id"] = default_address.id

        return redirect("order_confirmation")

    return render(
        request,
        "orders/checkout.html",
        {
            "cart_items": cart_items,
            "total": total,
            "default_address": default_address,
        }
    )
def order_confirmation(request):

    shipping_id = request.session.get('shipping_id')

    if not shipping_id:
        return redirect('checkout')

    address = ShippingAddress.objects.get(id=shipping_id)

    cart = request.session.get('cart', {})

    cart_items = []
    subtotal = 0

    for product_id, quantity in cart.items():

        product = Product.objects.get(id=product_id)

        item_total = product.selling_price * quantity

        subtotal += item_total

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': item_total
        })

    gst = subtotal * Decimal('0.05')

    if subtotal >= Decimal('799'):
        delivery_charge = Decimal('0')
    else:
        delivery_charge = Decimal('50')

    grand_total = subtotal + gst + delivery_charge

    context = {
        'address': address,
        'cart_items': cart_items,
        'subtotal': subtotal,
        'gst': f"{gst:.2f}",
        'delivery_charge': delivery_charge,
        'grand_total': f"{grand_total:.2f}",
        'order_id': f'FB{address.id:06}',
        'delivery_date': date.today() + timedelta(days=1),
    }

    return render(
        request,
        'orders/order_confirmation.html',
        context
    )


def login_view(request):
    return render(request, 'orders/login.html')


def create_account(request):
    return render(request, 'orders/create.html')