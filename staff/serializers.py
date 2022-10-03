from rest_framework import serializers
from staff.models import Worker, TabelWorkers


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = (
            'id', 'full_name',
            'image', 'job_title',
            'phone', 'email',
            'date_joined',
        )


class WorkerForTabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = (
            'id',
            'full_name',
            'job_title'
        )


class TabelWorkersSerializer(serializers.ModelSerializer):
    worker = WorkerForTabelSerializer(many=True)

    class Meta:
        model = TabelWorkers
        fields = (
            'id',
            'date',
            'total_quantity',
            'worker',
            'total_defect',
            'quantity_of_PU',
            'quantity_of_EVA',
            'price_of_single_mmodel',
            'total_price_of_one_worker',
            'final_salary_with_defect_calculation',
        )
