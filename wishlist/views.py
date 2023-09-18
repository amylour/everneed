from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from products.models import Product
from .models import Wishlist
from profiles.models import UserProfile


@login_required
def wishlist(request):
    """ A view to return the wishlist page """

    user_profile = UserProfile.objects.get(user=request.user)
    user_wishlist = Wishlist.objects.filter(user_profile=user_profile)

    return render(request, 'wishlist/wishlist.html', {'user_wishlist': user_wishlist})



@login_required
def add_to_wishlist(request, product_id):
    """
    Add a product to the user's wishlist.
    """
    product = get_object_or_404(Product, pk=product_id)
    user_profile = UserProfile.objects.get(user=request.user)

    # Check if the product is already in the users wishlist
    if Wishlist.objects.filter(user_profile=user_profile, product=product).exists():
        messages.warning(
            request, f'{product.name} is already in your Wishlist.')
    else:
        # create a new wishlist item
        wishlist_item = Wishlist.objects.create(
            user_profile=user_profile, product=product)
        messages.success(
            request, f'{wishlist_item.product.name} added to your Wishlist successfully!')

    # Redirect to the product detail page
    return redirect(reverse('product_detail', args=[product_id]))

    
