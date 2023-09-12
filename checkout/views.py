from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NpVS0JbjLH7yZ9O79zvpPgR9Y1ZcPE8VowtCMxGuj6Y6K7S3DaUSxHOZ8IFLPvUCVNtjmUIduXs5rajvsyIXTHg00NPF3usLU',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
