from django.shortcuts import render, redirect
from django.contrib import messages

def shopping_cart(request):
    """ a view to return shopping cart"""

    return render(request, 'shopping_cart/cart.html')


def add_to_cart(request, club_id):
    quantity = 1
    cart = request.session.get('cart', {})

    """
    if cart.items():
        # insert toast here (error)
        return redirect('clubs')
    """
    
    cart[club_id] = cart.get(club_id, quantity)
    messages.success(request, f'Added club to your bag')

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect('shopping_cart')