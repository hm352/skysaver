"""
Request wrappers to the Skyscanner API
"""

import requests
import json
from time import sleep


def create_session(data):
    """
        Creates session with Skyscanner API; sessions are polled for
        real time flight information in a given date range.
        create_session is called by travel_options.
    """
    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/pricing/v1.0"

    headers = {
        "X-RapidAPI-Host": "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        "X-RapidAPI-Key": "d6a92afd29msh6816f4510a93926p15a997jsncef016cde055",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    outbound = data.get('from_date')
    inbound = data.get('to_date')
    adults = data.get("adults")
    children = data.get("children")

    data = {
        "inboundDate": inbound,
        "cabinClass": "economy",
        "children": children,
        "infants": 0,
        "country": "UK",
        "currency": "GBP",
        "locale": "en-GB",
        "originPlace": "SFO-sky",
        "destinationPlace": "LHR-sky",
        "outboundDate": outbound,
        "adults": 1
    }
    response = requests.post(url, headers=headers, data=data)
    location = response.headers["Location"]
    sessionkey = location.split("/")[-1]
    return sessionkey


def travel_options(data):
    """
        Retrieves all potential routes for a given
        date range by polling a session 
    """
    sessionkey = create_session(data)
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


def get_places(query="Stockholm"):
    url = f"https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/UK/GBP/en-GB/?query={query}"
    headers = {
        "X-RapidAPI-Host": "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        "X-RapidAPI-Key": "d6a92afd29msh6816f4510a93926p15a997jsncef016cde055",
    }

    response = requests.get(url, headers=headers)
    content = json.loads(response.text)
    return content
