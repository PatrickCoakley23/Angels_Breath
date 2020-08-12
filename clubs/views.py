from django.shortcuts import render, get_object_or_404
from .models import Whiskey_club, Subscription_type


# Create your views here.


def whiskey_clubs(request):
    """ a view to return the different whiskey clubs users can subscribe to"""

    whiskey_clubs = Whiskey_club.objects.all()

    context = {
        'whiskey_clubs': whiskey_clubs,
    }

    return render(request, 'clubs/whiskey_clubs.html', context)


def club_selected(request, club_id):
    """ a view to return a more detailed look at the whiskey club selected"""

    club_selected = get_object_or_404(Whiskey_club, pk=club_id)
    
    context = {
        'club_selected': club_selected,
    }

    return render(request, 'clubs/whiskey_selected.html', context)


def choose_subscription(request, club_id):
    """ a view to show the subscription options """

    club_selected = get_object_or_404(Whiskey_club, pk=club_id) #picks up the specific whiskey selected id

    subscriptions = Subscription_type.objects.all() #this gets all the information like price, subsciption time(3 months/ 6months etc)

    context = {
        'club_selected': club_selected,
        'subscriptions': subscriptions,
    }

    return render(request, 'clubs/subscription_type.html', context)
