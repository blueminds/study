from rest_framework import serializers
from registros import models

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Curso
        fields = ('nombre','precio', 'numero_horas_total', 'numero_horas_semana', 'pais','escuela', 'fecha_creacion',)
