from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import ProductForm


def all_products(request):
    """ A view to return the products page, sorting and search queries """

    products = Product.objects.all()
    query = None
    # Fix: 'UnboundLocalError' -> credit: https://tinyurl.com/yc847kb7
    # & https://tinyurl.com/26a5ksrd
    categories = []  # Default value to initialize as an empty list
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

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

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


@login_required
def admin_product_list(request):
    """ A view to show an alphabetical list of products for admin """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    products = Product.objects.all().order_by('name')
    context = {
        'products': products,
    }

    return render(request, 'products/admin_product_list.html', context)


def product_detail(request, product_id):
    """ A view to return an individual products page """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


# Admin product detai view accessible via admin dashboard
@login_required
def admin_product_detail(request, product_id):
    """ A view to return an individual product's page for admin """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only store owners can access this page.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }

    return render(request, 'products/admin_product_detail.html', context)


@login_required
def admin_dashboard(request):
    """ A view to return the admin dashboard """

    if not request.user.is_superuser:
        return HttpResponseForbidden(
            "You do not have permission to "
            "access this page."
        )

    return render(request, 'products/admin_dashboard.html')


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product added successfully!')
            # Redirecting to admin_product_detail instead of product_detail
            return redirect(reverse('admin_product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.'
            )
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product successfully updated!')
            # Redirecting to admin_product_detail instead of product_detail
            return redirect(reverse('admin_product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.'
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('admin_product_list'))
