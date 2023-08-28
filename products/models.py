from django.db import models


class Category(models.Model):
    """ Category Models """
    # class constants for category names as strings 
    # django docs -> https://tinyurl.com/aprpz8rd
    WEAR = 'wear'
    CARE = 'care'
    EAT = 'eat'
    TRAVEL = 'travel'

    # tuple with constant-value pairs for each category of products
    CATEGORY_CHOICES = [
        (WEAR, 'Wear'),
        (CARE, 'Care'),
        (EAT, 'Eat'),
        (TRAVEL, 'Travel'),
    ]

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254, choices=CATEGORY_CHOICES)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        """ Method to return category friendly name """
        return self.friendly_name


class Product(models.Model):
    """ Model for everneed products """
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(
        max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField(max_length=1024, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sale_price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    discount = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    shoe_size = models.CharField(max_length=10, choices=[
        ('32-34', '32-34'),
        ('35-36', '35-36'),
        ('38-40', '38-40'),
        ('41-43', '41-43'),
        ('44-46', '44-46'),
    ], blank=True)
    clothes_size = models.CharField(max_length=2, choices=[
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
    ], blank=True)
    carbon_fp = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)
    carbon_saved = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    image_url = models.URLField(
        max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    feature_product = models.BooleanField(default=False, blank=True) 
    is_sale = models.BooleanField(default=False)

    def __str__(self):
        return self.name

