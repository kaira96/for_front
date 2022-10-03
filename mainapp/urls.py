from rest_framework.routers import DefaultRouter

from mainapp.views import (
    SemifinishedViewSet, CatalogViewSet,
    ElaborationViewSet, CountryViewSet,
    BrandViewSet
)


router = DefaultRouter()

router.register('countries', CountryViewSet, basename='countries')
router.register('semifinished', SemifinishedViewSet, basename='semifinished')
router.register('catalog', CatalogViewSet, basename='catalog')
router.register('elaboration', ElaborationViewSet, basename='elaboration')
router.register('brands', BrandViewSet, basename='brands')

urlpatterns = []

urlpatterns += router.urls
