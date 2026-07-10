from django.shortcuts import render, redirect
from products.models import Product

def checkout(request):

    cart = request.session.get('cart', {})

    cart_items = []
    total = 0

    for product_id, quantity in cart.items():

        product = Product.objects.get(id=product_id)

        subtotal = product.selling_price * quantity

        total += subtotal

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })

    return render(
        request,
        'orders/checkout.html',
        {
            'cart_items': cart_items,
            'total': total
        }
    )