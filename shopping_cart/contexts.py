from django.conf import settings
from django.shortcuts import get_object_or_404
from clubs.models import Subscription_type, Whiskey_club


def cart_contents(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    subscription_count = 0
    delivery = 0

    for sub_id, quantity in cart.items():
        subscription = get_object_or_404(Subscription_type, pk=sub_id)
        #club = subscription.whiskey_clubs.filter(pk=club_id)
        

        total += quantity * subscription.price
        cart_items.append(
            {   
                'sub_id': sub_id,
                'quantity': quantity,
                'subscription': subscription,
                #'club': club,
            }
        )

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'subscription_count': subscription_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
