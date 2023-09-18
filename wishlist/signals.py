from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Wishlist


@receiver(post_save, sender=Wishlist)
def create_wishlist_on_first_item_added(sender, instance, created, **kwargs):
    if created:
        user_profile = instance.user_profile
        if not user_profile.user_wishlist.exists():
            # Create a new Wishlist for the user if they don't have one
            Wishlist.objects.create(
                user_profile=user_profile, product=instance.product)
