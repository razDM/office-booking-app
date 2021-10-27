from django import forms
from datetime import datetime
from django.core.exceptions import ValidationError
from offices.models import Reservation
from selection.models import Office


class AvailabilityForm(forms.Form):
    start_date = forms.DateTimeField(required=True, input_formats=["%Y-%m-%d", "%Y-%m-%d"],
                                     widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    end_date = forms.DateTimeField(required=True, input_formats=["%Y-%m-%d", "%Y-%m-%d"],
                                   widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filter_list = kwargs['available_offices']

    def check_business_days(self, start, end):
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')
        if not(start_date < start and end_date < end):
            raise ValidationError(
                "Times beyond business days, please enter value within working days")
        else:
            return self.cleaned_data
