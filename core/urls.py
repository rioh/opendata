from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns(
    '',
    url(r'^$', views.homepage, name='homepage'),
    url(r'^browse/events$', views.browse, {'browse_type': "events"}, name='browse_events'),
    url(r'^browse/drugs$', views.browse, {'browse_type': "labels"}, name='browse_drugs'),
    url(r'^browse/enforcements$', views.browse, {'browse_type': "enforcements"}, name='browse_enforcements'),
    url(r'^search$', views.search, name='search'),
)
