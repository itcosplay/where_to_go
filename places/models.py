from django.db import models
from django.db.models.deletion import CASCADE


class Place(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='название'
        
    )
    description_short = models.CharField(
        max_length=500,
        verbose_name='краткое описание'
        
    )
    description_long = models.TextField(
        verbose_name='полное описание'
    )
    latitude = models.FloatField(
        verbose_name='lat'
    )
    lontitude = models.FloatField(
        verbose_name='lng'
    )

    def __str__(self):
        return f'{self.title}'


class Image(models.Model):
    title = models.ForeignKey(
        'Place',
        related_name='images',
        on_delete=CASCADE,
        verbose_name='название'

    )
    img = models.ImageField(
        verbose_name='изображение'
    )
    order_number = models.IntegerField(
        verbose_name='порядковый номер'
    )

    def __str__(self):
        return f'{self.title}'