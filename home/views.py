from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib import messages
from django.shortcuts import render, redirect
from products.models import Product
from django.http import HttpResponseRedirect


def index(request):
    """ A view to return the index page & display bestsellers """
    feature_products = Product.objects.filter(feature_product=True)

    context = {
        'feature_products': feature_products,
    }

    return render(request, 'home/index.html', context)


# Contact Us Form
def contact_form(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Contact Form Submission"
            body = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            send_mail(subject, message, 'everneed@example.com',
                      ['everneed@example.com'])

            messages.success(request, "Thanks for contacting us!")
            return render(request, 'home/thank_you.html')


    # redirect back to the previous page
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def terms_conditions(request):
    return render(request, 'home/terms_conditions.html')


def thank_you(request):
    return render(request, 'thank_you.html')





