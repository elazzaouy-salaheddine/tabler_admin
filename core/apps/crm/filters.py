import django_filters
from .models import Lead

class LeadFilter(django_filters.FilterSet):
    status = django_filters.ChoiceFilter(choices=Lead.status)
    created_at = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Lead
        fields = ['status', 'created_at']
