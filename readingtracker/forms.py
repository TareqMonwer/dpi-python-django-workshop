from django import forms
from .models import Plan


class PlanCreateForm(forms.ModelForm):
    time_starts = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
    time_ends = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])

    class Meta:
        model = Plan
        fields = ['plan_name', 'time_starts', 'time_ends', 'label', 'is_active']
    
    