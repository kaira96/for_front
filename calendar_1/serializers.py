from rest_framework import serializers

from calendar_1.models import (
    ElaborationCalendar, 
    ModelCalendarPU,
    ModelCalendarEVA
)

from mainapp.serializers import (
    CalendarCatalogSerializer,
)


class ElaborationCalendarSerializer(serializers.ModelSerializer):
    catalog = CalendarCatalogSerializer(many=True)
    elaboration_quantity = serializers.ReadOnlyField(
        source='elaboration.quantity_of_pairs_with_defect_calculation'
    )

    class Meta:
        model = ElaborationCalendar
        fields = (
            'id',
            'catalog',
            'date',
            'elaboration_quantity'
        )


class CalendarPUSerializer(serializers.ModelSerializer):
    catalog = CalendarCatalogSerializer(many=True)

    class Meta:
        model = ModelCalendarPU
        fields = (
            'id',
            'catalog',
            'quantity_of_PU',
            'date',
        )


class CalendarEVASerializer(serializers.ModelSerializer):
    catalog = CalendarCatalogSerializer(many=True)

    class Meta:
        model = ModelCalendarEVA
        fields = (
            'id',
            'catalog',
            'quantity_of_EVA',
            'date',
        )
