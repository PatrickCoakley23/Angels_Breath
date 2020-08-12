from django.shortcuts import render, redirect


def shopping_cart(request):
    """ a view to return shopping cart"""

    return render(request, 'shopping_cart/cart.html')


def add_to_cart(request, club_id):
    """ Add club before deciding subscription"""
    quantity = 1
    cart = request.session.get('cart', {})

    """
    if cart.items():
        # insert toast here (error)
        return redirect('clubs')
    """
    
    cart[club_id] = cart.get(club_id, quantity)

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect('shopping_cart')