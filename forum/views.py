from django.shortcuts import render


def forum(request):
    """ A view to return the forum page """
    return render(request, 'forum/forum.html')


def add_thread(request):
    """ A view to return the add_thread page """
    return render(request, 'forum/add_thread.html')
