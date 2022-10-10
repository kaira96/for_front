from django.urls import path

from rest_framework.routers import DefaultRouter

from users.views import UserReadOnlyViewSet, UserCreateAPIView


router = DefaultRouter()

router.register('users', UserReadOnlyViewSet)

urlpatterns = [
    path('registration/', UserCreateAPIView.as_view(), name='register'),
]

urlpatterns += router.urls
