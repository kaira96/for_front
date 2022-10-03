from rest_framework import serializers

from sales_.models import SaleWorker


class SaleWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleWorker
        fields = (
            'id', 'worker', 
            'catalog',
            'pairs_shoes', 'price',
            'sum_of_price'
        )
