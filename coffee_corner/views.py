from django.shortcuts import render


def coffee_corner(request):
    """ A view to return the coffee_corner page """
    return render(request, 'coffee_corner/coffee_corner.html')
