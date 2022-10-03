from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from stocks.models import StockOfDoneProducts
from stocks.serializers import StockOfDoneProductsSerializer
from stocks.permissions import IsStockManOrAdmin


class StockOfDoneProductsViewSet(ReadOnlyModelViewSet):
    queryset = StockOfDoneProducts.objects.all()
    serializer_class = StockOfDoneProductsSerializer
    permission_classes = (IsStockManOrAdmin,)
