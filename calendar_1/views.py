from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.viewsets import ReadOnlyModelViewSet

from calendar_1.models import ElaborationCalendar, ModelCalendarPU, ModelCalendarEVA
from calendar_1.serializers import ElaborationCalendarSerializer, CalendarPUSerializer, CalendarEVASerializer
from calendar_1.filters import CalendarFilter, CalendarPUFilter, CalendarEVAFilter


class ElaborationCalendarViewSet(ReadOnlyModelViewSet):
    queryset = ElaborationCalendar.objects.all()
    serializer_class = ElaborationCalendarSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CalendarFilter


class ModelCalendarPUViewSet(ReadOnlyModelViewSet):
    queryset = ModelCalendarPU.objects.all()
    serializer_class = CalendarPUSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CalendarPUFilter


class ModelCalendarEVAViewSet(ReadOnlyModelViewSet):
    queryset = ModelCalendarEVA.objects.all()
    serializer_class = CalendarEVASerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CalendarEVAFilter
