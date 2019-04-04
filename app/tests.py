from django.test import TestCase
import json
from .emmissions import count_stops


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
        stops = count_stops(itinerary, legs)
        self.assertEqual(stops, 2)
