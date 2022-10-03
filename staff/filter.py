from django_filters import rest_framework as filters

from staff.models import TabelWorkers


class TableWorkersFilter(filters.FilterSet):
    class Meta:
        model = TabelWorkers
        fields = ('date',)
