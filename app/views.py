from django.shortcuts import render, redirect
from .travel import travel_options
from .emissions import get_inbound_leg, get_outbound_leg, route_finder, route_emissions


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

        for itinerary in itineraries:
            leg = get_outbound_leg(itinerary, legs)
            stops = count_stops(leg)
        return render(
            request,
            "app/results.html",
            context={"itineraries": itineraries}
        )
