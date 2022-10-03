from rest_framework import viewsets 
from rest_framework.response import Response

from daily_diary.models import DailyDiary
from daily_diary.serializers import (
    DailyDiarySerializer,
    ListDailyDiarySerializer
)


class DailyDiaryViewSet(viewsets.ModelViewSet):
    queryset = DailyDiary.objects.all()
    serializer_class = DailyDiarySerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = ListDailyDiarySerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ListDailyDiarySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ListDailyDiarySerializer(instance)
        return Response(serializer.data)
