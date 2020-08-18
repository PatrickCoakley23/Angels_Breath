from django.shortcuts import get_object_or_404
from clubs.models import Subscription_type, Whiskey_club, Subscriptions


# Cart items defined so they can be accessed across the site
def cart_contents(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    delivery = 0

    for sub_id, sub_details in cart.items():
        subscription = get_object_or_404(Subscription_type, pk=sub_id)
        club = get_object_or_404(Whiskey_club, pk=sub_details['club_id'])
        all_subs = Subscription_type.objects.all()
      
        total += sub_details['quantity'] * subscription.price
        cart_items.append(
            {
                'sub_id': sub_id,
                'quantity': sub_details['quantity'],
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
