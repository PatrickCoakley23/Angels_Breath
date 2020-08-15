from django.shortcuts import get_object_or_404
from clubs.models import Subscription_type, Whiskey_club, Subscriptions

# Cart items defined so they can be accessed across the site


def cart_contents(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    subscription_count = 0
    delivery = 0

# sub_id is the id of the Subscription_type id
# passed from the subscription_type.html
    for sub_id, sub_details in cart.items():
        subscription = get_object_or_404(Subscription_type, pk=sub_id)
        club = get_object_or_404(Whiskey_club, pk=sub_details['club_id'])
        #club = subscription.whiskey_clubs.filter(club_subs=sub_id)
        #club = Whiskey_club.objects.filter(club_subs=sub_id)
       
        

        total += sub_details['quantity'] * subscription.price
        cart_items.append(
            {
                'sub_id': sub_id,
                'quantity': sub_details['quantity'],
                'subscription': subscription,
                'club': club,
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
