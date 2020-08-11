def cart_contents(request):

    cart_items = []
    total = 0
    subscription_count = 0

    context = {
        'cart_items': cart_items,
        'total': total,
        'subscription_count': subscription_count,
    }

    return context
