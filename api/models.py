from django.db import models


class ProductSet(models.Model):
    """ Продуктовый набор. """

    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание', blank=True)


class Recipient(models.Model):
    """ Получатель. """

    surname = models.CharField('Фамилия', max_length=30)
    name = models.CharField('Имя', max_length=30)
    patronymic = models.CharField('Отчество', max_length=30)
    phone_number = models.CharField('Телефон', max_length=30)
    delivery_address = models.CharField('Адрес доставки', max_length=500)


class Order(models.Model):
    """ Заказ. """

    STATUS_CHOICES = [
        ('CR', 'created'),
        ('DE', 'delivered'),
        ('PR', 'processed'),
        ('CA', 'cancelled')
    ]

    order_created_datetime = models.DateTimeField()
    delivery_datetime = models.DateTimeField()
    recipient = models.ForeignKey(
        Recipient,
        verbose_name='Получатель',
        on_delete=models.CASCADE,
        related_name='order'
    )
    product_set = models.ForeignKey(
        ProductSet,
        verbose_name='Набор продуктов',
        on_delete=models.CASCADE,
        related_name='order'
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)

