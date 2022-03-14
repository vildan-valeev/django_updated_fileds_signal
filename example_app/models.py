from django.db import models

from example_app.tracker import track_data


class ItemType(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['id']
        verbose_name = 'Тип товара'
        verbose_name_plural = 'Типы товаров'

    def __str__(self):
        return self.name


def get_common_user():
    obj, created = ItemType.objects.get_or_create(name='Дефолтный товар')
    return obj


@track_data('name', 'item_type',)
class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя', null=True, blank=True)
    item_type = models.ForeignKey(ItemType, on_delete=models.SET_DEFAULT, verbose_name='Тип товара',
                                  default=get_common_user, related_name='items')
    created = models.DateTimeField(auto_now_add=True, editable=False, null=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, editable=False, null=True, verbose_name='Обновлен')

    def __str__(self):
        return f'{self.name} | {self.item_type}'

    class Meta:
        ordering = ['id']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
