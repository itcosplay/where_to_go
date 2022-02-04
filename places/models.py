from django.db import models


class Place(models.Model):
    title = models.CharField(
        verbose_name='название',
        max_length=200
    )
    description_short = models.CharField(
        verbose_name='краткое описание',
        max_length=500
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