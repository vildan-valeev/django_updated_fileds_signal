from django.db.models.signals import post_save
from django.dispatch import receiver

from example_app.models import Item


@receiver(post_save, sender=Item)
def post_save_order(sender, instance: Item, created, **kwargs):
    print('Item post save signal')
