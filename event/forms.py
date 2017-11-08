from django import forms
from django.contrib.admin import widgets
from .models import EventLocation, EventManager


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class EventManagerForm(forms.ModelForm):

    class Meta:
        model = EventManager
        fields =['title', 'description', 'event_start_time', 'event_end_time', 'event_date']

        widgets = {
            'event_date': DateInput(),
            'event_start_time': TimeInput(),
            'event_end_time': TimeInput(),
        }

    # def __init__(self, *args, **kwargs):
    #     super(EventManagerForm, self).__init__(*args, **kwargs)
    #     self.fields['event_date'].widget = widgets.AdminDateWidget()
    #     self.fields['event_start_time'].widget = widgets.AdminTimeWidget()
    #     self.fields['event_end_time'].widget = widgets.AdminTimeWidget()


class EventLocationForm(forms.ModelForm):

    class Meta:
        model = EventLocation
        fields = ['address', 'city', 'zip_code']
