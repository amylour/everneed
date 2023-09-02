from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category



def all_products(request):
    """ A view to return the products page, sorting and search queries """

    products = Product.objects.all()
    query = None
    # Fix: 'UnboundLocalError' -> credit: https://tinyurl.com/yc847kb7
    # & https://tinyurl.com/26a5ksrd
    categories = [] # Default value to initialize as an empty list

    if request.GET:
        if 'category' in request.GET:
            selected_categories = request.GET.getlist('category')
            if 'all' in selected_categories:
                products = products  # Don't filter for 'all' categories
            else:
                products = products.filter(
                    category__name__in=selected_categories)
                categories = Category.objects.filter(
                    name__in=selected_categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "Please enter an item to search for.")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to return an individual products page """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
