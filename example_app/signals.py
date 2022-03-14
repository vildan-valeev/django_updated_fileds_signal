from django.db.models.signals import post_save
from django.dispatch import receiver

from example_app.models import Item, User


@receiver(post_save, sender=Item)
def post_save_order(sender, instance: Item, created, **kwargs):
    print('Item post save signal')
    if created:
        print('Item created')
    else:

        print('Item updated', instance.whats_changed())
        if instance.has_changed('amount'):
            user = User.objects.get(pk=instance.user_id)
            user.balance -= instance.amount
            user.save()
