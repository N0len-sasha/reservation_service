from django.db import models


class Room(models.Model):

    price = models.FloatField(
        "Цена за ночь",
    )
    description = models.TextField(
        "Описание"
    )
    create_date = models.DateField(
        "Дата добавления",
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'


class Reservation(models.Model):

    hotel_id = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Номер'
    )
    date_start = models.DateField(
        "Дата начала брони",
    )
    date_end = models.DateField(
        "Дата окончания брони"
    )

    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Брони'
