from rest_framework import viewsets
from . import models, serializers


# Create your views here.
class TareaViewSet(viewsets.ModelViewSet):
    queryset = models.Tarea.objects.all()
    serializer_class = serializers.TareaModelSerializer
