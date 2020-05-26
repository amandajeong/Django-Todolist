from django import forms
from django.forms import ModelForm

from .models import *


class Taskform(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Add new task...'
    }))

    due_date = forms.DateField(widget=forms.SelectDateWidget, required=False)

    class Meta:
        model = Task
        fields = '__all__'