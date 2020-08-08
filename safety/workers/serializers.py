from rest_framework.serializers import ModelSerializer

from rest_framework import serializers

from .models import Worker


class WorkerSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    is_available = serializers.BooleanField()
    primary_phone = serializers.CharField()
    secondary_phone = serializers.CharField()
    address = serializers.CharField()

class WorkerModelSerializer(ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'
