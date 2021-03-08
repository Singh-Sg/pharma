from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from precscription.models import Precscription, Drug, Order

# method for creating order for current saved precscription.
@receiver(post_save, sender=Precscription)
def add_order(sender, instance, created, raw, **kwargs):
    if created:
        Order.objects.create(user=instance.patient.user, precscriptions=instance, ordered=True)
    # TODO
    else:
        pass
