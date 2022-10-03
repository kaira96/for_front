from rest_framework import serializers

from daily_diary.models import DailyDiary

from staff.serializers import WorkerForTabelSerializer

from mainapp.serializers import CalendarCatalogSerializer


class DailyDiarySerializer(serializers.ModelSerializer):

    class Meta:
        model = DailyDiary

        # catalog = CalendarCatalogSerializer(many=True)

        fields = (
            'id',
            'catalog',
            'price', 
            'date', 
            'worker',
            'package_pairs',
            'quantity_of_PU',
            'quantity_of_EVA',
            'quantity_of_pairs',
            'semifinished',
            'SAYA_defect', 
            'PU_defect', 
            'EVA_defect',
            'total_PU',
            'total_EVA',
            'package',
            'worker_defect',
            'total_defect',
            'total_price',
            'to_stock'
        )

        extra_kwargs = {
            'semifinished': {'write_only': True},
        }


class ListDailyDiarySerializer(serializers.ModelSerializer):
    semifinished_title = serializers.ReadOnlyField(
        source='semifinished.title'
    )

    catalog = CalendarCatalogSerializer(many=True)
    worker = WorkerForTabelSerializer(many=True)

    class Meta:
        model = DailyDiary
        fields = (
            'id',
            'catalog',
            'price', 
            'date', 
            'worker',
            'package_pairs',
            'quantity_of_PU',
            'quantity_of_EVA',
            'quantity_of_pairs',
            'semifinished',
            'semifinished_title',
            'SAYA_defect', 
            'PU_defect', 
            'EVA_defect',
            'total_PU',
            'total_EVA',
            'package',
            'worker_defect',
            'total_defect',
            'total_price',
            'to_stock'
        )
