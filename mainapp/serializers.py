from django.forms import ValidationError
from rest_framework import serializers

from mainapp.models import (
    Semifinished,
    Catalog, Elaboration,
    Country, Brand
)


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = (
            'id', 'title'
        )


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            'id', 'title'
        )


class SemifinishedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Semifinished
        fields = (
            'id', 'title', 'quantity',
            'date', 'country', 'total_rest'
        )


class CatalogSerializer(serializers.ModelSerializer):
    articul_title = serializers.ReadOnlyField(
            source='articul.title'
        )

    class Meta:
        model = Catalog
        fields = (
            'id', 'model', 'color',
            'picture', 'size_from', 'size_to',
            'articul', 'articul_title'
        )

        extra_kwargs = {
            'articul': {'write_only': True}
        }

    def validate(self, attrs):
        size_from = attrs.get('size_from')
        size_to = attrs.get('size_to')
        sizes = range(30, 46)
        if size_from not in sizes or size_to not in sizes:
            raise ValidationError('Input acceptable sizes')
        return attrs


class CalendarCatalogSerializer(serializers.ModelSerializer):
    articul = serializers.ReadOnlyField(
            source='articul.title'
        )

    class Meta:
        model = Catalog
        fields = (
            'id', 
            'model',
            'articul',
            'color'
        )


class ElaborationSerializer(serializers.ModelSerializer):
    semifinished_quantity = serializers.ReadOnlyField(
        source='semifinished.quantity'
    )
    catalog = CalendarCatalogSerializer(many=True)

    class Meta:
        model = Elaboration
        fields = (
            'id', 'semifinished',
            'semifinished_quantity',
            'quantity_of_pairs',
            'quantity_of_packages',
            'catalog', 'defect_working',
            'defect_EVA', 'defect_PU',
            'date', 'total_defect',
        )
