from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.urls import reverse

from places.models import Place


def get_place_by_id(request, place_id):
    place = get_object_or_404(Place, pk=place_id)

    detailsUrl = {
        "title": place.title,
        "imgs": [img.img.url for img in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lontitude,
            "lat": place.latitude
        }
    }

    return JsonResponse(
        detailsUrl, safe=False,
        json_dumps_params={
            'ensure_ascii': False,
            'indent': 2
        }
    )


def serialize_place_data(place):
    
    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [
                place.lontitude,
                place.latitude
            ],
        },
        "properties": {
            "title": place.title,
            "placeId": place.pk,
            "detailsUrl": reverse('place_by_id', args=[place.pk])
        }
    }


def main_page(request):
    places = Place.objects.all()

    context = {
        "type": "FeatureCollection",
        "features": [
            serialize_place_data(place) for place in places
        ]
    }    

    return render(request, 'index.html', {'places': context})