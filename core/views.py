from django.shortcuts import render


def homepage(request):
    return render(request, 'core/homepage.html')


def browse_events(request):
    return render(request, 'core/browse_events.html')


def browse_drugs(request):
    return render(request, 'core/browse_drugs.html')


def browse_enforcements(request):
    return render(request, 'core/browse_enforcements.html')


def search(request):
    return render(request, 'core/search_results.html')


def result(request):
    return render(request, 'core/result.html')
