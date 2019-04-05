from django.test import TestCase
from django.core.cache import cache
from django.conf import settings
import json
from .emissions import (
    count_stops,
    get_outbound_leg,
    route_finder,
    IATA_mapping,
    route_emissions
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
        expected = [['SFO', 'ZRH'], ['ZRH', 'LHR']]
        leg = get_outbound_leg(itinerary, legs)
        route = route_finder(leg, places)
        self.assertEqual(route, expected)
        emissions = route_emissions(route)
        assert emissions < 2500

    def test_airport_name_mapping(self):
        expected = "LIS"
        code = 4609
        airport = IATA_mapping(code, places)
        self.assertEqual(airport, expected)
