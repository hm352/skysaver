from django.shortcuts import render, redirect
from .travel import travel_options


def form(request):
    if request.method == "GET":
        return render(request, "app/form.html")


def results(request):
    if request.method == "GET":
        return redirect("/")

    else:
        content = travel_options()
        itineraries = content["Itineraries"]
        return render(
            request,
            "app/results.html",
            context={"itineraries": itineraries}
        )
