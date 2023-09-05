from django import forms
from .models import *

class CreateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('user','company') # hariç tut

class UpdateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('user','company') # hariç tut