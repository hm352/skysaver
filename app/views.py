from time import sleep
import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .travel import travel_options, get_places
from .emissions import (
    get_inbound_leg,
    get_outbound_leg,
    route_finder,
    route_emissions,
    count_stops
)

@csrf_exempt
def form(request):
    if request.method == "GET":
        return render(request, "app/form.html", {'form': form})
    else:
        outbound_date = request.POST.get("from")
        inbound_date = request.POST.get("to")

        content = travel_options("2019-09-15", "2019-09-20")

        itineraries = content["Itineraries"]
        legs = content["Legs"]
        places = content["Places"]

        for itinerary in itineraries:
            out_leg = get_outbound_leg(itinerary, legs)
            stops = count_stops(out_leg)
            itinerary["Connections"] = stops
            out_route = route_finder(out_leg, places)
            emissions = route_emissions(out_route)
            itinerary["Emissions"] = emissions
            itinerary["Price"] = itinerary["PricingOptions"][0]["Price"]
            itinerary["Departure"] = out_leg["Departure"]
        return HttpResponse(json.dumps(itineraries))


@csrf_exempt
def places(request):
    query = request.body.decode()
    places = get_places(query)["Places"]
    place_list = [place["PlaceName"] for place in places]
    if not place_list:
        place_list = ["destination does not exist :("]
    return HttpResponse(place_list)
