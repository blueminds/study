from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from registros import models
import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
import json
# Create your views here.




class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class CursoList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def post(self, request, format=None):
        body = request.body
        body = json.loads(body)
        filter = body


        cursos = models.Curso.objects.filter(precio__lte = filter['precio_maximo'], precio__gte = filter['precio_minimo'])
        serializer = serializers.CursoSerializer(cursos, many=True)
        return JSONResponse(serializer.data)
