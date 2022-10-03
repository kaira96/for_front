from rest_framework import serializers

from stocks.models import StockOfDoneProducts

from mainapp.serializers import CalendarCatalogSerializer


class StockOfDoneProductsSerializer(serializers.ModelSerializer):
    catalog = CalendarCatalogSerializer(many=True)

    class Meta:
        model = StockOfDoneProducts
        fields = (
            'id', 'quantity', 
            'date', 'catalog',
            'total_rest'
        )
