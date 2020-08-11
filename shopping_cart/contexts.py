from django.conf import settings
from django.shortcuts import get_object_or_404
from clubs.models import Whiskey_club


def cart_contents(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    subscription_count = 0

    for club_id, quantity in cart.items():
        whiskey_club = get_object_or_404(Whiskey_club, pk=club_id)
        total += quantity 
        cart_items.append(
            {
                'club_id': club_id,
                'quantity': quantity,
                'whiskey_club': whiskey_club,
            }
        )

    context = {
        'cart_items': cart_items,
        'total': total,
        'subscription_count': subscription_count,
    }

    return context
