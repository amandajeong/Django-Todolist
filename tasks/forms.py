from django import forms
from django.forms import ModelForm

from .models import *


class Taskform(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Add new task...'
    }))

    due_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'datepicker'}))

    class Meta:
        model = Task
        fields = {
            'title': Task.title,
            'due_date': Task.due_date,
            'complete': Task.complete
            }
