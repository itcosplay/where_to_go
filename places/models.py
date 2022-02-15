from turtle import title
from django.db import models
from django.db.models.deletion import CASCADE
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='название'
        
    )
    description_short = models.TextField(
        blank=True,
        verbose_name='краткое описание'
        
    )
    description_long = HTMLField(
        blank=True,
        verbose_name='полное описание'
    )
    latitude = models.FloatField(
        verbose_name='lat'
    )
    longitude = models.FloatField(
        verbose_name='lng'
    )

    def __str__(self):
        return self.title

    class Meta:
        unique_together = (
            ('longitude', 'latitude')
        )


class Image(models.Model):
    place = models.ForeignKey(
        'Place',
        related_name='images',
        on_delete=CASCADE,
        verbose_name='название'
    )
    img = models.ImageField(
        verbose_name='изображение'
    )
    position = models.IntegerField(
        default=0,
        verbose_name='позиция'
    )
    
    def __str__(self):
        return str(self.place)

    class Meta:
        ordering = ['position']