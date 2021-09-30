from django.shortcuts import render


def forum(request):
    """ A view to return the forum page """
    return render(request, 'forum/forum.html')
