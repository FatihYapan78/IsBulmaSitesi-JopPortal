import django_filters
from .models import *
from django import forms

class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    salary = django_filters.RangeFilter()
    job_type = django_filters.ModelMultipleChoiceFilter(
        queryset=JobType.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
    )
    location = django_filters.ModelMultipleChoiceFilter(
        queryset=Location.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
    )
    industry = django_filters.ModelMultipleChoiceFilter(
        queryset=Industry.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
    )
    class Meta:
        model = Job
        fields = ["title","salary","job_type","location","industry"]