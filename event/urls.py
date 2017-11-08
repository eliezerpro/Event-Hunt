from django.conf.urls import url
from .views import home, event_detail, error, event_list


urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^list/$', event_list, name="list"),
    url(r'^detail/(?P<event_slug>[-\w]+)/$', event_detail, name="details"),
    url(r'^error/$', error, name="error"),
]

# url(r'^category/(?P<category_slug>[-\w]+)/$', category, name='category'),