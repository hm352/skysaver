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


def route_finder(leg, places):
    stops = leg["Stops"]
    origin = leg["OriginStation"]
    destination = leg["DestinationStation"]
    stops.insert(0, origin)
    stops.append(destination)
    route = []
    for i, _ in enumerate(stops):
        if i > 0:
            from_ = IATA_mapping(stops[i - 1], places)
            to = IATA_mapping(stops[i], places)
            node = [from_, to]
            route.append(node)
    return route


def IATA_mapping(code, places):
    for place in places:
        if place["Id"] == code:
            return place["Code"]


def route_emissions(route):
    total_emissions = 0
    for node in route:
        total_emissions += emissions(node[0], node[1])
    return total_emissions


def emissions(origin, destination, seat_class="economy"):
    url = "http://impact.brighterplanet.com/flights.json"
    params = {
        "origin_airport": f"{origin}",
        "destination_airport": f"{destination}",
        "trips": 1,
        "seat_class": seat_class
    }
    response = requests.post(url, params=params)
    emmissions = json.loads(response.text)
    carbon = emmissions["decisions"]["carbon"]["object"]["value"]
    return carbon
