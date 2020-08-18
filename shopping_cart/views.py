from django.shortcuts import render, redirect, get_object_or_404, reverse, HttpResponse
from django.contrib import messages
from clubs.models import Subscription_type, Whiskey_club, Subscriptions
from checkout.models import OrderLineItem


def shopping_cart(request):
    """ a view to return shopping cart"""

    return render(request, 'shopping_cart/cart.html')


def add_to_cart(request, sub_id, club_id):
    """Most of this functions variables are derived from
    the contexts processor in contexts.py.
    (shopping cart app). This is so the shopping bag,
    is made available across the website.
    """

    # Cart is a dictionary and the objects are a dictionary nested within the cart dictionary
    quantity = 1
    cart = request.session.get('cart', {})
    clubs_in_cart = []
    for subscription, sub_details in cart.items():
        clubs_in_cart.append(sub_details['club_id'])

    # Prevents Users from having two of the same whiskey_clubs in the cart
    if club_id in clubs_in_cart:
        messages.error(request, "You've already got a subscription to that club in your cart!")
        return redirect(reverse('clubs'))

    # Checks to see if you have that club already in an order on our database
    club = get_object_or_404(Whiskey_club, pk=club_id)  
    existing_subs = OrderLineItem.objects.filter(
        user_profile=request.user.userprofile,
        whiskey_club=club,
    )
    if existing_subs:
        messages.error(request, "You've already got a subscription to that club on our database!")
        return redirect(reverse('clubs'))

 


    cart[sub_id] = cart.get(sub_id, {
        'club_id': club_id,
        'quantity': quantity
        })

    messages.success(request, 'Added club to your bag')

    request.session['cart'] = cart
    return redirect('shopping_cart')


def update_cart(request, club_id):
    quantity = 1
    cart = request.session.get('cart', {})
    old_sub_id = request.POST.get('current_sub_id')

    del cart[old_sub_id]

    new_sub_id = request.POST['change_subscription'] # here i am changing the sub_id depending on the value selected in the dropdown

    cart[new_sub_id] = cart.get(new_sub_id, {
        'club_id': club_id,
        'quantity': quantity,
        })

   
    request.session['cart'] = cart
    return redirect(reverse('shopping_cart'))


def delete_sub(request, club_id, sub_id):
    cart = request.session.get('cart', {})
    
    print(club_id)
    print(sub_id)

    del cart[sub_id]
    request.session['cart'] = cart
    return redirect(reverse('shopping_cart'))
    
    





    

