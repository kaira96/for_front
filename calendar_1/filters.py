from django_filters import rest_framework as filters

from calendar_1.models import ElaborationCalendar, ModelCalendarEVA, ModelCalendarPU


class CalendarFilter(filters.FilterSet):
    date_month = filters.NumberFilter(
        field_name='date__month', lookup_expr='exact')

    class Meta:
        model = ElaborationCalendar
        fields = ('date_month', 'date')


class CalendarPUFilter(filters.FilterSet):
    date_month = filters.NumberFilter(
        field_name='date__month', lookup_expr='exact')

    class Meta:
        model = ModelCalendarPU
        fields = ('date_month', 'date')


class CalendarEVAFilter(filters.FilterSet):
    date_month = filters.NumberFilter(
        field_name='date__month', lookup_expr='exact')

    class Meta:
        model = ModelCalendarEVA
        fields = ('date_month', 'date')
