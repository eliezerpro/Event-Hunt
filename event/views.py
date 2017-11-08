from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.http import Http404
from .models import EventManager, EventLocation
from django.db.models import Q
from.forms import EventManagerForm, EventLocationForm


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


def event_create(request):
    if not request.user.is_active or not request.user.is_authenticated:
        return redirect("events_app:error")
    form1 = EventManagerForm(request.POST or None)
    form2 = EventLocationForm(request.POST or None)

    if form1.is_valid() and form2.is_valid():
        instance1 = form1.save(commit=False)
        instance2 = form2.save(commit=False)
        instance1.save()
        instance2.title_id = instance1.id
        instance2.save()
        return HttpResponseRedirect(instance1.get_absolute_url())

    context = {"form1": form1, "form2": form2}
    return render(request, 'event/event_form.html', context)

def event_update(request, event_slug):
    if not request.user.is_active or not request.user.is_authenticated:
        return redirect("events_app:error")
    main_instance = get_object_or_404(EventManager, slug=event_slug)
    location_instances = get_object_or_404(EventLocation, title_id= main_instance.id)
    form1 = EventManagerForm(request.POST or None, instance=main_instance)
    form2 = EventLocationForm(request.POST or None, instance=location_instances)

    if form1.is_valid() and form2.is_valid():
        instance1 = form1.save(commit=False)
        instance2 = form2.save(commit=False)
        instance1.save()
        instance2.title_id = instance1.id
        instance2.save()
        return HttpResponseRedirect(instance1.get_absolute_url())

    context = {"form1": form1, "form2": form2}
    return render(request, 'event/event_form.html', context)

def event_delete(request):
    pass

def error(request):
    return render(request, 'event/error.html', context={})
