from django.shortcuts import render


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def faq(request):
    """ A view to return the FAQ page """

    return render(request, 'home/faq.html')
