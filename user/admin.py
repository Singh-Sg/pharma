from django.contrib import admin
from .models import User, Doctor, Patient

# Register User model to admin.
admin.site.register(User)

# Register Patient model to admin.
admin.site.register(Patient)

# Register Doctor model to admin.
admin.site.register(Doctor)
