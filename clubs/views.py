from django.shortcuts import render, get_object_or_404
from .models import Whiskey_club, Subscription_type


def whiskey_clubs(request):
    """
    A view which renders all the whiskey clubs on "Choose Your Posion" Page.
    """

    whiskey_clubs = Whiskey_club.objects.all()
    
    context = {
        'whiskey_clubs': whiskey_clubs,
    }

    return render(request, 'clubs/whiskey_clubs.html', context)


def club_selected(request, club_id):
    """
    This view grabs the id of the whiskey_club selected
    and brings the user to a more page
    with more details on that whiskey
    """

    club_selected = get_object_or_404(Whiskey_club, pk=club_id)

    context = {
        'club_selected': club_selected,
    }

    return render(request, 'clubs/whiskey_selected.html', context)


def choose_subscription(request, club_id):
    """ This view collects the id of the Whiskey type the
        user has chosen and
        lists all the subscription types available
    """
    club_selected = get_object_or_404(Whiskey_club, pk=club_id)
    # picks up the specific whiskey selected id

    subscriptions = Subscription_type.objects.all()
    # this gets all the information like price,
    # subscription time(3 months/ 6months etc)

    context = {
        'club_selected': club_selected,
        'subscriptions': subscriptions,
    }

    return render(request, 'clubs/subscription_type.html', context)
