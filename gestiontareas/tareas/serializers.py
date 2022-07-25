from rest_framework import serializers
from . import models


class TareaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tarea
        fields = '__all__'
