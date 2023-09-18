from profiles.models import UserProfile
from .models import Wishlist


def wishlist_items(request):
    """ Wishlist items context processor """
    wishlist_items = []

    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        wishlist_items = Wishlist.objects.filter(user_profile=user_profile)

    return {
        'user_wishlist': wishlist_items,
    }
