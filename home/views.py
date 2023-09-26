from django.shortcuts import render
from products.models import Product


def index(request):
    """ A view to return the index page & display bestsellers """
    feature_products = Product.objects.filter(feature_product=True)

    context = {
        'feature_products': feature_products,
    }

    return render(request, 'home/index.html', context)


