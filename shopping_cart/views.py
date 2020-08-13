from django.shortcuts import render, redirect
from django.contrib import messages

def shopping_cart(request):
    """ a view to return shopping cart"""

    return render(request, 'shopping_cart/cart.html')


def add_to_cart(request, sub_id):
    quantity = 1
    cart = request.session.get('cart', {})
    

    """
    if cart.items():
        # insert toast here (error)
        return redirect('clubs')
    """
    
    cart[sub_id ] = cart.get(sub_id, quantity)
    messages.success(request, f'Added club to your bag')

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect('shopping_cart')