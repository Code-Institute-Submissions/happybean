"""
Views for About Pages including Our Story, FAQ & Contact Form
"""

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm


def about(request):
    """ A view to return the about page """
    return render(request, 'about/about.html')


def our_story(request):
    """
    A view to return the our_story page
    """
    return render(request, 'about/our_story.html')


def faq(request):
    """
    A view to return the faq page
    """
    return render(request, 'about/faq.html')


# Original Code with modifications from https://bit.ly/3BM12q2
def contact_view(request):
    """
    A view to return the contact form
    """
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, [
                    'happybean.info@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "about/contact_us.html", {'form': form})


def success_view(request):
    """
    A view to return the success page after an email was sent.
    """
    return render(request, 'about/contact_success.html')
