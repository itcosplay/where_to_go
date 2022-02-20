from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.urls import reverse

from places.models import Place


def get_place_by_id(request, place_id):
    place = get_object_or_404(Place, pk=place_id)

    details = {
        "title": place.title,
        "imgs": [img.img.url for img in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.longitude,
            "lat": place.latitude
        }
    }

    return JsonResponse(
        details, safe=False,
        json_dumps_params={
            'ensure_ascii': False,
            'indent': 2
        }
    )


def get_geojson_about_place(place):
    
    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [
                place.longitude,
                place.latitude
            ],
        },
        "properties": {
            "title": place.title,
            "placeId": place.pk,
            "detailsUrl": reverse('place_by_id', args=[place.pk])
        }
    }


def render_main_page(request):
    places = Place.objects.all()

    context = {
        "type": "FeatureCollection",
        "features": [
            get_geojson_about_place(place) for place in places
        ]
    }    

    return render(request, 'index.html', {'places': context})