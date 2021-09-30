from django.shortcuts import render


def forum(request):
    """ A view to return the forum page """
    return render(request, 'forum/forum.html')


def add_thread(request):
    """ A view to return the add_thread page """
    return render(request, 'forum/add_thread.html')


def thread(request):
    """ A view to return the thread page """
    return render(request, 'forum/thread.html')


def add_comment(request):
    """ A view to return the add_comment page """
    return render(request, 'forum/add_comment.html')
