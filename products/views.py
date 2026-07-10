from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.shortcuts import redirect
from django.db.models import Q
from decimal import Decimal

def search_products(request):
    query = request.GET.get('q', '').strip()

    products = Product.objects.all()

    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(category__name__icontains=query)
        )

    return render(
        request,
        'products/search_results.html',
        {
            'query': query,
            'products': products
        }
    )


def add_to_cart(request, product_id):

    product = Product.objects.get(id=product_id)

    if product.stock <= 0 or not product.is_available:
        return redirect('product_detail', product_id)
    
    quantity = int(request.POST.get('quantity', 1))

    cart = request.session.get('cart', {})

    product_id = str(product_id)

    current_qty = cart.get(product_id, 0)

    if current_qty + quantity <= product.stock:

        if product_id in cart:
            cart[product_id] += quantity
        else:
            cart[product_id] = quantity

        request.session['cart'] = cart

    return redirect('cart')

def category_products(request, pk):

    category = get_object_or_404(Category, pk=pk)

    products = Product.objects.filter(
        category=category,
        is_available=True
    )

    return render(
        request,
        'products/category_products.html',
        {
            'category': category,
            'products': products
        }
    )


def product_detail(request, pk):

    product = get_object_or_404(Product, pk=pk)

    return render(
        request,
        'products/product_detail.html',
        {
            'product': product
        }
    )

def cart(request):

    cart = request.session.get('cart', {})

    cart_items = []

    subtotal = Decimal('0.00')

    for product_id, quantity in cart.items():

        try:
            product = Product.objects.get(id=product_id)

            item_total = product.selling_price * quantity

            subtotal += item_total

            cart_items.append({
                'product': product,
                'quantity': quantity,
                'subtotal': item_total
            })

        except Product.DoesNotExist:
            pass

    # GST 5%
    gst = subtotal * Decimal('0.05')

    # Delivery Charge
    if subtotal == 0:
        delivery_charge = Decimal('0.00')
    elif subtotal >= Decimal('799.00'):
        delivery_charge = Decimal('0.00')
    else:
        delivery_charge = Decimal('40.00')

    grand_total = subtotal + gst + delivery_charge

    return render(
        request,
        'products/cart.html',
        {
            'cart_items': cart_items,
            'subtotal': subtotal.quantize(Decimal('0.01')),
            'gst': gst.quantize(Decimal('0.01')),
            'delivery_charge': delivery_charge.quantize(Decimal('0.01')),
            'grand_total': grand_total.quantize(Decimal('0.01')),
        }
    )

def increase_cart(request, product_id):

    cart = request.session.get('cart', {})

    product_id = str(product_id)

    if product_id in cart:
        cart[product_id] += 1

    request.session['cart'] = cart

    return redirect('cart')


def decrease_cart(request, product_id):

    cart = request.session.get('cart', {})

    product_id = str(product_id)

    if product_id in cart:

        cart[product_id] -= 1

        if cart[product_id] <= 0:
            del cart[product_id]

    request.session['cart'] = cart

    return redirect('cart')


def remove_cart(request, product_id):

    cart = request.session.get('cart', {})

    product_id = str(product_id)

    if product_id in cart:
        del cart[product_id]

    request.session['cart'] = cart

    return redirect('cart')