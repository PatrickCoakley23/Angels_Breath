from django.shortcuts import render
from .models import whiskey_club


# Create your views here.


def whiskey_clubs(request):
    """ a view to return the different whiskey clubs users can subscribe to"""
    
    whiskey_clubs = whiskey_club.objects.all()

    context = {
        'whiskey_clubs': whiskey_clubs,
    }

    return render(request, 'clubs/whiskey_clubs.html', context)
