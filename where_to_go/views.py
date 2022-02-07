from django.shortcuts import render

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