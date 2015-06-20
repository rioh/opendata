import requests

from django.shortcuts import render
from django.conf import settings


BROWSE_TYPES = {
    "events": "%s?count=patient.reaction.reactionmeddrapt.exact" % settings.FDA_DRUG_API_EVENT_URL, 
    "labels": "%s?count=openfda.substance_name.exact" % settings.FDA_DRUG_API_LABEL_URL,
    "enforcements": "%s?count=recalling_firm.exact" % settings.FDA_DRUG_API_ENFORCEMENT_URL}


def homepage(request):
    return render(request, 'core/homepage.html')


def browse(request, browse_type):
    data = {}
    events = requests.get(BROWSE_TYPES.get(browse_type))
    if events:
        events_json = events.json()
        data['terms'] = [event.get('term') for event in events_json.get('results')]
    return render(request, 'core/browse.html', data)


def search(request):
    if request.method == 'GET' and 'q' in request.GET:
        query_string = request.GET.get('q').strip()
        data = {'q': query_string}

        enforcements = requests.get("%s?search=%s&limit=100" % (settings.FDA_DRUG_API_ENFORCEMENT_URL, query_string)).json()
        data['enforcement_results'] = enforcements.get('results')

        events = requests.get("%s?search=%s&limit=100" % (settings.FDA_DRUG_API_EVENT_URL, query_string)).json()
        data['event_results'] = events.get('results')
 
        labels = requests.get("%s?search=%s&limit=100" % (settings.FDA_DRUG_API_LABEL_URL, query_string)).json()
        data['label_results'] = labels.get('results')

    return render(request, 'core/search_results.html', data)


def result(request):
    return render(request, 'core/result.html')
