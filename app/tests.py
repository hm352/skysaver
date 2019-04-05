from django.test import TestCase
import json
from .emmissions import (
    count_stops,
    get_inbound_leg,
    get_outbound_leg,
    route_finder
)


def load_data():
    with open("app/test_data.json") as file:
        data = json.load(file)
    itineraries = data["Itineraries"]
    legs = data["Legs"]
    places = data["Places"]
    return (itineraries, legs, places)


itineraries, legs, places = load_data()


class test_emissions(TestCase):
    def test_load_data(self):
        self.assertIsNotNone(itineraries)
        self.assertIsNotNone(legs)
        self.assertIsNotNone(places)

    def test_get_stops(self):
        itinerary = itineraries[0]
        leg = get_outbound_leg(itinerary, legs)
        stops = count_stops(leg)
        self.assertEqual(stops, 1)

    def test_route_finder(self):
        itinerary = itineraries[0]
        expected = [[16216, 18563], [18563, 13554]]
        leg = get_outbound_leg(itinerary, legs)
        route = route_finder(leg)
        self.assertEqual(route, expected)
