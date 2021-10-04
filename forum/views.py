from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ThreadForm, CommentForm

from .models import Thread, Comment


def forum(request):
    """ A view to return the forum page """
    model = Thread
    template_name = "forum/forum.html"

    context = {
        'object_list': Thread.objects.all(),
    }

    return render(request, 'forum/forum.html', context)


def add_thread(request):
    """ A view to return the add_thread page """
    model = Thread
    form_class = ThreadForm
    success_message = "Thread '%(title)s' was created successfully"
    template_name = "forum/add_thread.html"

    return render(request, 'forum/add_thread.html')


def thread(request):
    """ A view to return the thread page """
    model = Thread
    template_name = "forum/thread.html"

    return render(request, 'forum/thread.html')


def add_comment(request):
    """ A view to return the add_comment page """
    model = Comment
    template_name = "forum/add_comment.html"
    success_message = "Your comment was added successfully"
    form_class = CommentForm

    return render(request, 'forum/add_comment.html')
