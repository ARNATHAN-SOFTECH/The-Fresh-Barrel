from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.shortcuts import redirect
from django.db.models import Q

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

    product = get_object_or_404(Product, id=product_id)

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

    product = get_object_or_404(
        Product,
        pk=pk,
        is_available=True
    )

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
        'products/cart.html',
        {
            'cart_items': cart_items,
            'total': total
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