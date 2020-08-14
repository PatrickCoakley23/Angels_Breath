from django.shortcuts import render, redirect
from django.contrib import messages


def shopping_cart(request):
    """ a view to return shopping cart"""

    return render(request, 'shopping_cart/cart.html')


def add_to_cart(request, sub_id):
    """Most of this functions variables are derived from
    the contexts processor in contexts.py
    in the shopping cart app. This is so the shopping bag,
    is made available across the website.
    """

    quantity = 1
    cart = request.session.get('cart', {})

    """
    if cart.items():
        # insert toast here (error)
        return redirect('clubs')
    """

    cart[sub_id] = cart.get(sub_id, quantity)
    messages.success(request, 'Added club to your bag')

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect('shopping_cart')
