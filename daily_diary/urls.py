from rest_framework.routers import DefaultRouter
# from django.urls import path

from daily_diary.views import DailyDiaryViewSet


router = DefaultRouter()

router.register('daily-diary', DailyDiaryViewSet, basename='daily-diary')

urlpatterns = []

urlpatterns += router.urls
