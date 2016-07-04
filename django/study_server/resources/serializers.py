from rest_framework import serializers
from model import models

class CursoSerializer(serializers.ModelSerializer):
    actividades = serializers.StringRelatedField(many=True)
    class Meta:
        model = models.Curso
        fields = ('id', 'nombre','precio', 'numero_horas_total', 'numero_horas_semana', 'pais','escuela', 'actividades', 'fecha_creacion',)
