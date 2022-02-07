from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from places.models import Place


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
            "detailsUrl": "./static/where_to_go/places/moscow_legends.json"
        }
    }


def main_page(request):
    places = Place.objects.all()

    context = {
        'type': 'FeatureCollection',
        'features': [
            serialize_place_data(place) for place in places
        ]
    }    

    return render(request, 'index.html', {'places': context})


def get_place_by_id(request, place_id):
    place = get_object_or_404(Place, pk=place_id)

    context = {
        'title': place.title,
        'imgs': [img.img.url for img in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.lontitude,
            'lat': place.latitude
        }
    }

    return JsonResponse(
        context, safe=False,
        json_dumps_params={
            'ensure_ascii': False,
            'indent': 2
        }
    )