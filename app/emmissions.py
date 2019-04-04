import json
import requests


def parse_leg(itinerary, legs):
    outbound_id = itinerary["OutboundLegId"]
    inbound_id = itinerary["InboundLegId"]
    for leg in legs:
        if leg["Id"] == outbound_id:
            outbound_stops = leg["Stops"]
        if leg["Id"] == outbound_id:
            inbound_stops = leg["Stops"]
    return inbound_stops, outbound_stops


def count_stops(itinerary, legs):
    outbound_stops, inbound_stops = parse_leg(itinerary, legs)
    stops = len(outbound_stops) + len(inbound_stops)
    return stops


def route_finder():
    pass

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
