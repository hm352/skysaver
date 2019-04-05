import json
import requests
from itertools import cycle


def get_leg(id, legs):
    for leg in legs:
        if leg["Id"] == id:
            return leg


def get_outbound_leg(itinerary, legs):
    outbound_id = itinerary["OutboundLegId"]
    return get_leg(outbound_id, legs)


def get_inbound_leg(itinerary, legs):
    inbound_id = itinerary["InboundLegId"]
    return get_leg(inbound_id, legs)


def count_stops(leg):
    stops = leg["Stops"]
    return len(stops)


def route_finder(leg):
    stops = leg["Stops"]
    origin = leg["OriginStation"]
    destination = leg["DestinationStation"]
    stops.insert(0, origin)
    stops.append(destination)
    route = []
    for i, _ in enumerate(stops):
        if i > 0:
            node = [stops[i - 1], stops[i]]
            route.append(node)
    return route


def emmissions(origin, destination):
    url = "http://impact.brighterplanet.com/flights.json"
    params = {
        "origin_airport": f"{orgin}",
        "destination_airport": f"{destination}",
        "trip": 1
    }
    response = requests.post(url, params=params)
    emmissions = json.loads(response.text)
    carbon = emmissions["decisions"]["carbon"]["object"]["value"]
