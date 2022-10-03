from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser

from django_filters.rest_framework import DjangoFilterBackend


from mainapp.models import (
    Semifinished,
    Catalog, Elaboration,
    Country, Brand
)
from mainapp.serializers import (
    SemifinishedSerializer, CatalogSerializer,
    ElaborationSerializer, CountrySerializer,
    BrandSerializer
)
from mainapp.filters import ElaborationFilter


class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class SemifinishedViewSet(ModelViewSet):
    queryset = Semifinished.objects.all()
    serializer_class = SemifinishedSerializer


class CatalogViewSet(ModelViewSet):
    parser_classes = [MultiPartParser, FormParser]
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer


class ElaborationViewSet(ReadOnlyModelViewSet):
    queryset = Elaboration.objects.all()
    serializer_class = ElaborationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ElaborationFilter


