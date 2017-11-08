from django.conf.urls import url
from .views import home, event_detail, error, event_list, event_create, event_delete, event_update


urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^list/$', event_list, name="list"),
    url(r'^detail/(?P<event_slug>[-\w]+)/$', event_detail, name="details"),
    url(r'^create/$', event_create, name="create"),
    url(r'^(?P<event_slug>[-\w]+)/update/$', event_update, name="update"),
    url(r'^delete/(?P<event_slug>[-\w]+)/$', event_delete, name="delete"),
    url(r'^error/$', error, name="error"),
]
