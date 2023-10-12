from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

from products.models import Product


def bag(request):
    """ A view to return the bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the chosen product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    # get bag variable if it exists in this session
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(
                    request,
                    f'Updated {product.name}, size {size.upper()} '
                    f'quantity to {bag[item_id]["items_by_size"][size]}'
                )
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(
                    request,
                    f'Added {product.name}, size {size.upper()} to your bag'
                )
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(
                request,
                f'Added {product.name}, size {size.upper()} to your bag'
            )
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(
                request,
                f'Updated {product.name} quantity to {bag[item_id]}'
            )
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust quantity of item in shopping bag"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(
                request,
                f'Updated {product.name}, size {size.upper()} quantity to '
                f'{bag[item_id]["items_by_size"][size]}'
            )
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(
                request,
                f'Removed {product.name}, size {size.upper()} from your bag'
            )
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(
                request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('bag'))


def remove_from_bag(request, item_id):
    """Remove item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(
                request,
                f'Removed {product.name}, size {size.upper()}  from your bag')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
