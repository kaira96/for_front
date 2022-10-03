from rest_framework.routers import DefaultRouter

from stocks.views import StockOfDoneProductsViewSet


router = DefaultRouter()

router.register(
    'stock-of-done-products', 
    StockOfDoneProductsViewSet, 
    basename='stock-of-done-products'
)

urlpatterns = []

urlpatterns += router.urls
