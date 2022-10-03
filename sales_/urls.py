from rest_framework.routers import DefaultRouter

from sales_.views import SaleWorkerViewSet


router = DefaultRouter()

router.register('sales-journal', SaleWorkerViewSet)

urlpatterns = []

urlpatterns += router.urls
