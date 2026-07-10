from .models import Product

def cart_count(request):

    cart = request.session.get('cart', {})

    count = sum(cart.values())

    header_cart_items = []

    header_cart_total = 0

    for product_id, quantity in cart.items():

        try:
            product = Product.objects.get(id=product_id)

            subtotal = product.selling_price * quantity

            header_cart_total += subtotal

            header_cart_items.append({
                'product': product,
                'quantity': quantity,
                'subtotal': subtotal
            })

        except Product.DoesNotExist:
            pass

    return {
        'cart_count': count,
        'header_cart_items': header_cart_items,
        'header_cart_total': header_cart_total,
    }