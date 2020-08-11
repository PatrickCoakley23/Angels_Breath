from django.shortcuts import render


def shopping_cart(request):
    """ a view to return shopping cart"""

    return render(request, 'shopping_cart/cart.html')
