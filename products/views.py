from django.shortcuts import render

# Create your views here.


def products(request):
    """ A view to return the products page """

    return render(request, 'products/products.html')
