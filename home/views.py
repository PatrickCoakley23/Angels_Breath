from django.shortcuts import render


def index(request):
    """ a view to return index page"""

    return render(request, 'home/index.html')

def about(request):
    """ a view to return the 'How it Works' page"""

    return render(request, 'home/about.html')

def error(request):
    """ a view to return the 'How it Works' page"""

    return render(request, 'home/error_handler.html')

