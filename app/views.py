from django.shortcuts import render
import requests
from datetime import datetime

# Create your views here.
def home(request):

    # get world data
    url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/world"

    headers = {
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com",
        'x-rapidapi-key': "53261179d3msh4f625af6c821a4cp17aaa5jsn475301ddb7c1"
        }

    response = requests.request("GET", url, headers=headers).json()

    # get time/date
    last_updated = datetime.now()

    context = {
        'world_data' : response,
        'last_updated' : last_updated,
    }

    return render(request, 'app/index.html', context)

def asia(request):

    # get asia data
    url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/asia"

    headers = {
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com",
        'x-rapidapi-key': "53261179d3msh4f625af6c821a4cp17aaa5jsn475301ddb7c1"
        }

    response = requests.request("GET", url, headers=headers).json()

    # get time/date
    last_updated = datetime.now()

    context = {
        'asia_data' : response,
        'last_updated' : last_updated,
    }

    return render(request, 'app/asia.html', context)

def africa(request):

    # get africa data
    url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/africa"

    headers = {
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com",
        'x-rapidapi-key': "53261179d3msh4f625af6c821a4cp17aaa5jsn475301ddb7c1"
        }

    response = requests.request("GET", url, headers=headers).json()

    # get time/date
    last_updated = datetime.now()

    context = {
        'africa_data' : response,
        'last_updated' : last_updated,
    }

    return render(request, 'app/africa.html', context)

def europe(request):

    # get europe data
    url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/europe"

    headers = {
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com",
        'x-rapidapi-key': "53261179d3msh4f625af6c821a4cp17aaa5jsn475301ddb7c1"
        }

    response = requests.request("GET", url, headers=headers).json()

    # get time/date
    last_updated = datetime.now()

    context = {
        'europe_data' : response,
        'last_updated' : last_updated,
    }

    return render(request, 'app/europe.html', context)

def north_america(request):

    # get north america data
    url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/northamerica"

    headers = {
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com",
        'x-rapidapi-key': "53261179d3msh4f625af6c821a4cp17aaa5jsn475301ddb7c1"
        }

    response = requests.request("GET", url, headers=headers).json()

    # get time/date
    last_updated = datetime.now()

    context = {
        'north_america_data' : response,
        'last_updated' : last_updated,
    }

    return render(request, 'app/namerica.html', context)

def south_america(request):

    # south america data
    url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/southamerica"

    headers = {
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com",
        'x-rapidapi-key': "53261179d3msh4f625af6c821a4cp17aaa5jsn475301ddb7c1"
        }

    response = requests.request("GET", url, headers=headers).json()

    # get time/date
    last_updated = datetime.now()

    context = {
        'south_america_data' : response,
        'last_updated' : last_updated,
    }

    return render(request, 'app/samerica.html', context)

def australia_ocenia(request):

    # get australia and ocenia data
    url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/australia"

    headers = {
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com",
        'x-rapidapi-key': "53261179d3msh4f625af6c821a4cp17aaa5jsn475301ddb7c1"
        }

    response = requests.request("GET", url, headers=headers).json()

    # get time/date
    last_updated = datetime.now()

    context = {
        'ocenia_data' : response,
        'last_updated' : last_updated,
    }

    return render(request, 'app/austocenia.html', context)

def about(request):

    return render(request, 'app/about.html')

def covid_news(request):

    # get covid news
    url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/news/get-coronavirus-news/0"

    headers = {
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com",
        'x-rapidapi-key': "53261179d3msh4f625af6c821a4cp17aaa5jsn475301ddb7c1"
        }

    response = requests.request("GET", url, headers=headers).json()

    # get time/date
    published_on = datetime.now()

    context = {
        'news' : response['news'],
        'published_on' : published_on,
    }

    return render(request, 'app/news.html', context)

def health_news(request):

    # get health news
    url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/news/get-health-news/1"

    headers = {
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com",
        'x-rapidapi-key': "53261179d3msh4f625af6c821a4cp17aaa5jsn475301ddb7c1"
        }

    response = requests.request("GET", url, headers=headers).json()

    # get time/date
    published_on = datetime.now()

    context = {
        'news' : response['news'],
        'published_on' : published_on,
    }

    return render(request, 'app/news.html', context)

def vaccine_news(request):

    # get vaccine news
    url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/news/get-vaccine-news/0"

    headers = {
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com",
        'x-rapidapi-key': "53261179d3msh4f625af6c821a4cp17aaa5jsn475301ddb7c1"
        }

    response = requests.request("GET", url, headers=headers).json()

    # get time/date
    published_on = datetime.now()

    context = {
        'news' : response['news'],
        'published_on' : published_on,
    }

    return render(request, 'app/news.html', context)
