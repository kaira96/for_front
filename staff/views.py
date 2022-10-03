from rest_framework import viewsets

from django_filters.rest_framework import DjangoFilterBackend

from staff.serializers import *
from staff.models import *
from staff.filter import *
from staff.permissions import IsAccountantOrAdmin


class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


class TabelWorkersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TabelWorkers.objects.all()
    serializer_class = TabelWorkersSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TableWorkersFilter
    permission_classes = (IsAccountantOrAdmin,)
