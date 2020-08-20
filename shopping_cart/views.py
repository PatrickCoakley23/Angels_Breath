from django.shortcuts import (
    render, redirect,
    get_object_or_404, reverse
)
from django.contrib import messages
from clubs.models import Whiskey_club
from checkout.models import OrderLineItem


def shopping_cart(request):
    """ a view to return shopping cart"""

    return render(request, 'shopping_cart/cart.html')


def add_to_cart(request, sub_id, club_id):
    """Most of this functions variables are derived from
    the contexts processor in contexts.py.
    (shopping cart app). This is so the shopping bag,
    is made available across the website.

    Cart is a dictionary and the objects
    are a dictionary nested within the cart dictionary
    """

    quantity = 1
    cart = request.session.get('cart', {})

    if not request.user.is_authenticated:
        messages.error(request,
                       'you have to be logged in to add Whiskey clubs to cart')
        return redirect(reverse('account_login'))

    # Checks to see if you have that club already in an order on our database
    club = get_object_or_404(Whiskey_club, pk=club_id)
    existing_subs = OrderLineItem.objects.filter(
        user_profile=request.user.userprofile,
        whiskey_club=club,
    )
    if existing_subs:
        messages.error(request,
                       f"You've already got a subscription to {club.name}"
                       "on our database!")
        return redirect(reverse('clubs'))

    # Prevents Users from having two of the same whiskey_clubs in the cart
    if club_id in list(cart.keys()):
        messages.error(request,
                       "You've already got a subscription to "
                       f"{club.name} in your cart!")
        return redirect(reverse('clubs'))

    # Finally if passes all if statements, the subscription can be added
    cart[club_id] = cart.get(club_id, {
        'sub_id': sub_id,
        'quantity': quantity
        })

    messages.success(request, f'Added {club.name} to your bag')

    request.session['cart'] = cart
    return redirect('clubs')


def update_cart(request, club_id):
    """ A view to allow users update their subscription in the cart """

    cart = request.session.get('cart', {})
    new_sub_id = request.POST['change_subscription']

    # here i am changing the sub_id depending
    # on the value selected in the dropdown

    cart[club_id]['sub_id'] = new_sub_id

    request.session['cart'] = cart
    return redirect(reverse('shopping_cart'))


def delete_sub(request, club_id, sub_id):
    # A view to delete whiskey club subscriptions from the cart
    cart = request.session.get('cart', {})

    del cart[club_id]

    request.session['cart'] = cart
    return redirect(reverse('shopping_cart'))
