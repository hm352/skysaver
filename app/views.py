from django.shortcuts import render, redirect
from .travel import travel_options
from .emissions import (
    get_inbound_leg,
    get_outbound_leg,
    route_finder,
    route_emissions,
    count_stops
)


def form(request):
    if request.method == "GET":
        return render(request, "app/form.html")


def results(request):
    if request.method == "GET":
        return redirect("/")

    else:
        content = travel_options()
        itineraries = content["Itineraries"]
        legs = content["Legs"]
        places = content["Places"]
        price = []
        for itinerary in itineraries:
            out_leg = get_outbound_leg(itinerary, legs)
            stops = count_stops(out_leg)
            itinerary["Connections"] = stops
            out_route = route_finder(out_leg, places)
            emissions = route_emissions(out_route)
            itinerary["Emissions"] = emissions
            itinerary["Price"] = itinerary["PricingOptions"][0]["Price"]
        return render(
            request,
            "app/results.html",
            context = {
            "itineraries": itineraries
            }
        )
