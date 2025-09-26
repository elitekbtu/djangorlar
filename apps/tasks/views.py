# Python modules
from typing import Any
from datetime import datetime
import pytz

# Djando modules
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt


def welcome_view(
    request: HttpRequest,
    *args: tuple[Any, ...],
    **kwarg: dict[str, Any]
)->HttpResponse:
    """
    Welcome page view that's says welcome for everyone!

    Params:
        request: HttpRequest
            The request object.
        *args: list
            Additional positional arguments.
        **kwargs: dict
            Additional keyword arguments.
    """

    return render(
        request=request, 
        template_name="welcome.html", 
        context={"message": "Welcome bro, I'm happy see your in my project"},
        status=200,
    )

def users_view(
    request: HttpRequest,
    *args: tuple[Any, ...],
    **kwargs: dict[str, Any]
)->HttpResponse:
    """
    Users list view, that shows list of users

    Params:
        request: HttpRequest
            The request object.
        *args: list
            Additional positional arguments.
        **kwargs: dict
            Additional keyword arguments.
    """

    return render(
        request=request, 
        template_name="users.html", 
        context={"users": ["Arman", "Ermek", "Temirbolat", "Turarbek"]}, 
        status=200
    )

def city_time_view(
    request: HttpRequest,
    *args:tuple[Any, ...], 
    **kwargs: dict[str, Any]
) -> HttpResponse:
    
    """
    City time view, that shows time of the cities

    Params:
        request: HttpRequest
            The request object.
        *args: list
            Additional positional arguments.
        **kwargs: dict
            Additional keyword arguments.
    """

    tz_almaty = pytz.timezone("Asia/Almaty")
    tz_calgary = pytz.timezone("America/Edmonton") 
    tz_moscow = pytz.timezone("Europe/Moscow")
    tz_utc = pytz.UTC

    almaty_time = datetime.now(tz_almaty)
    calgary_time = datetime.now(tz_calgary)
    moscow_time = datetime.now(tz_moscow)
    utc_time = datetime.now(tz_utc)

    return render(
        request = request,
        template_name = "city-time.html",

        context = {
            "Almaty": almaty_time.strftime("%Y-%m-%d %H:%M:%S"),
            "Calgary": calgary_time.strftime("%Y-%m-%d %H:%M:%S"),
            "Moscow": moscow_time.strftime("%Y-%m-%d %H:%M:%S"),
            "UTC": utc_time.strftime("%Y-%m-%d %H:%M:%S"),
        }
    )

@csrf_exempt
def count_view(
    request:HttpRequest, 
    *args: tuple[Any, ...], 
    **kwargs: dict[str, Any]
) ->HttpResponse:
    """
    Count of clicks view, that shows count of clicks

    Params:
        request: HttpRequest
            The request object.
        *args: list
            Additional positional arguments.
        **kwargs: dict
            Additional keyword arguments.
    """

    clicks = request.session.get("clicks", 0)

    if request.method == "POST":
        clicks += 1
        request.session["clicks"] = clicks
        return HttpResponse(f"{clicks}")
    
    if request.method == "DELETE":
        request.session["clicks"] = 0
        return HttpResponse("0")

    return render(
        request=request, 
        template_name="count.html", 
        context={"count": clicks}, 
        status=200
    )





