from django.shortcuts import render


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


def contact_us(request):
    """
    A view to return the contact_us page
    """
    return render(request, 'about/contact_us.html') 
