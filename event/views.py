from django.shortcuts import render, get_object_or_404, redirect
from .models import EventManager, EventLocation
from django.db.models import Q


# Create your views here.

def home(request):
    latest_events = EventManager.objects.order_by('-event_date')[:10]
    context = {'latest_events': latest_events}
    return render(request, 'event/home.html', context)


def event_list(request):
    events = EventLocation.objects.all()[::-1]
    query = request.GET.get("q")
    if query:
        events = EventLocation.objects.all()
        events = events.filter(
            Q(address__icontains=query) |
            Q(states__icontains=query) |
            Q(city__icontains=query) |
            Q(zip_code__icontains=query) |
            Q(title__title__icontains=query)|
            Q(title__description__icontains=query)
        ).distinct()[::-1]
    context = {"event_list": events}
    return render(request, "event/list.html", context)


def event_detail(request, event_slug):
    if not request.user.is_active or not request.user.is_authenticated:
        return redirect("events_app:error")
    event = get_object_or_404(EventManager, slug=event_slug)
    address = event.eventlocation_set.all()
    context = {'event': event, 'address': address}
    return render(request, 'event/detail.html', context)


def error(request):
    return render(request, 'event/error.html', context={})
