from .forms import ContactForm

# Return contact form across website
def contact_form(request):
    form = ContactForm()
    return {'contact_form': form}
