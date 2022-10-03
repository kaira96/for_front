from rest_framework.routers import DefaultRouter

from calendar_1.views import (
    ElaborationCalendarViewSet, 
    ModelCalendarPUViewSet,
    ModelCalendarEVAViewSet
)


router = DefaultRouter()

router.register('calendar-elaboration', ElaborationCalendarViewSet)
router.register('calendar-PU', ModelCalendarPUViewSet)
router.register('calendar-EVA', ModelCalendarEVAViewSet)

urlpatterns = []
urlpatterns += router.urls
