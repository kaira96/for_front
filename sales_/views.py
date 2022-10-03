from rest_framework.viewsets import ModelViewSet

from sales_.models import SaleWorker
from sales_.serializers import SaleWorkerSerializer


class SaleWorkerViewSet(ModelViewSet):
    queryset = SaleWorker.objects.all()
    serializer_class = SaleWorkerSerializer
