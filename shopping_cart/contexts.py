from django.shortcuts import get_object_or_404
from clubs.models import Subscription_type, Whiskey_club

"""
Making use of Contexts processor so the cart items
defined below are made available across the entire
website
"""


def cart_contents(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    delivery = 0

    """
    This is how the clubs are added to the cart.
    for club_id, club_details in cart.items():
    {'1':{'sub_id':4', 'quantity':1}}
    """

    for club_id, club_details in cart.items():
        club = get_object_or_404(Whiskey_club, pk=club_id)
        subscription = get_object_or_404(
                        Subscription_type, pk=club_details['sub_id']
                        )
        all_subs = Subscription_type.objects.all()

        total += club_details['quantity'] * subscription.price
        cart_items.append(
            {
                'club_id': club_id,
                'quantity': club_details['quantity'],
                'subscription': subscription,
                'club': club,
                'all_subs': all_subs,
            }
        )

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'delivery': delivery,
        'grand_total': grand_total,
    }
    return context
