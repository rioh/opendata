import logging

from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from .api_client import ApiClient


logger = logging.getLogger(__name__)


def homepage(request):
    return render(request, 'core/homepage.html')


def browse(request, browse_type):
    logger.debug("browsing %s", browse_type)
    client = ApiClient()
    data = {'terms': client.browse(browse_type)}
    return render(request, 'core/browse.html', data)


def search(request):
    if request.method == 'GET' and 'q' in request.GET:
        query_string = request.GET.get('q').strip()
        client = ApiClient()

        return render(request, 'core/search_results.html', client.search(query_string))


def result(request):
    return render(request, 'core/result.html')


def search_detail(request):
    results = {}
    if request.method == 'GET' and 'q' in request.GET:
        q = request.GET.get('q').strip()
        filter_string = request.GET.get('filter_string').strip()
        client = ApiClient()
        results = client.get_age_sex(q, filter_string)
    return HttpResponse(results, content_type='application/json')
