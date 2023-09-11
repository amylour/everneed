from django.apps import AppConfig

#  override the ready method to import signals model so every time a
#  line item is saved or deleted, the update total model method is updated
class CheckoutConfig(AppConfig):
    name = 'checkout'

    def ready(self):
        import checkout.signals

