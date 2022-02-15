from urllib.parse import urlparse

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place, Image


class Command(BaseCommand):
    help = 'Download place(s) by url(urls).json'

    def add_arguments(self, parser):
        parser.add_argument('urls', nargs='+', type=str)

    def handle(self, urls, *args, **kwargs):
        for url in urls:
            load_place(url)


def load_place(url):
    response = requests.get(url)
    response.raise_for_status()

    place_data = response.json()

    title = place_data['title']
    description_short = place_data['description_short']
    description_long = place_data['description_long']
    latitude = place_data['coordinates']['lat']
    longitude = place_data['coordinates']['lng']

    place, created = Place.objects.get_or_create(
        latitude=float(latitude),
        longitude=float(longitude),
        defaults={
            'title': title,
            'description_short': description_short,
            'description_long': description_long
        }
    )

    if not created: return

    for url in place_data['imgs']:
        image_name = urlparse(url).path.split('/')[-1]

        response = requests.get(url)
        response.raise_for_status()

        image = Image(place=place)
        image.img.save(
            image_name,
            ContentFile(response.content),
            save=True
        )