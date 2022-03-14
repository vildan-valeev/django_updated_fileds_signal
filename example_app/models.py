from django.db import models

from example_app.tracker import track_data


class User(models.Model):
    name = models.CharField(max_length=50)
    balance = models.IntegerField()

    class Meta:
        ordering = ['id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.name


def get_common_user():
    obj, created = User.objects.get_or_create(name='Дефолтный юзер', balance=5000)
    return obj


@track_data('name', 'user', 'amount')
class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, verbose_name='Тип товара',
                             default=get_common_user, related_name='items')
    amount = models.IntegerField(verbose_name='Цена')
    created = models.DateTimeField(auto_now_add=True, editable=False, null=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, editable=False, null=True, verbose_name='Обновлен')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['id']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
