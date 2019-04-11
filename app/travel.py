import requests
import json
from time import sleep


def create_session(outbound, inbound):
    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/pricing/v1.0"

    headers = {
        "X-RapidAPI-Host": "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        "X-RapidAPI-Key": "d6a92afd29msh6816f4510a93926p15a997jsncef016cde055",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "inboundDate": inbound,
        "cabinClass": "business",
        "children": 0,
        "infants": 0,
        "country": "US",
        "currency": "USD",
        "locale": "en-US",
        "originPlace": "SFO-sky",
        "destinationPlace": "LHR-sky",
        "outboundDate": outbound,
        "adults": 1
    }

    response = requests.post(url, headers=headers, data=data)
    location = response.headers["Location"]
    sessionkey = location.split("/")[-1]
    return sessionkey


def travel_options(outbound, inbound):
    sessionkey = create_session(outbound, inbound)
    headers = {
        "X-RapidAPI-Host": "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        "X-RapidAPI-Key": "d6a92afd29msh6816f4510a93926p15a997jsncef016cde055",
    }
    get_url = f"https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/pricing/uk2/v1.0/{sessionkey}?pageIndex=0&pageSize=10"

    polling = True

    # potential concern with the implementation is different content is
    # returned at each poll, hence current logic block causes
    # data loss
    while polling:
        r = requests.get(get_url, headers=headers)
        content = json.loads(r.text)
        status = content["Status"]
        if status == "UpdatesComplete":
            polling = False
            return content
