import json


def load_data():
    with open("test_data.json") as file:
        data = json.load(file)
    itinerary = data["itinerary"]
    legs = data["Legs"]
    places = data["places"]
    return (itinerary, legs, places)


def get_stops( itinerary, legs):
	pass