from rest_framework.routers import DefaultRouter

from staff.views import TabelWorkersViewSet, WorkerViewSet

router = DefaultRouter()

router.register('tabel-workers', TabelWorkersViewSet)
router.register('workers', WorkerViewSet)

urlpatterns = []

urlpatterns += router.urls