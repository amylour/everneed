from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    total_carbon_fp = 0
    total_carbon_saved = 0  

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
            # Calculate carbon footprint of order and carbon saved
            total_carbon_fp += (item_data *
                                product.carbon_fp) if product.carbon_fp else 0
            total_carbon_saved += (item_data *
                                   product.carbon_saved) if product.carbon_saved else 0
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })
                total_carbon_fp += (quantity *
                                    product.carbon_fp) if product.carbon_fp else 0
                total_carbon_saved += (quantity *
                                       product.carbon_saved) if product.carbon_saved else 0

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total
    # display bag item quantity on bag icon
    total_item_count = sum(item.get('quantity', 0) for item in bag_items)

    context = {
        'bag_items': bag_items,
        'total': total,
        'total_item_count': total_item_count,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'total_carbon_fp': total_carbon_fp,
        'total_carbon_saved': total_carbon_saved,
    }

    return context
