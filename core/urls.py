from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns(
    '',
    url(r'^$', views.homepage, name='homepage'),
    url(r'^browse/events$', views.browse_events, name='browse_events'),
    url(r'^browse/drugs$', views.browse_drugs, name='browse_drugs'),
    url(r'^browse/enforcements$', views.browse_enforcements, name='browse_enforcements'),
    url(r'^search$', views.search, name='search'),
    url(r'^result$', views.result, name='result'),
)
