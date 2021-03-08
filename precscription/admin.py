from django.contrib import admin
from .models import Precscription, Drug, Order

# Register Precscription model to admin.
admin.site.register(Precscription)

# Register Drug model to admin.
admin.site.register(Drug)

# Register Order model to admin.
admin.site.register(Order)