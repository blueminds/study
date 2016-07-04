from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from model import models
import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
import json
from django.db.models import Q
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
    def get(self, request, format=None):
        #return HttpResponse("ok")
        #body = request.body
        #body = json.loads(body)
        #filter = body
        #cursos = models.Curso.objects.filter(
        #    precio__lte = filter['precio_maximo'],
        #    precio__gte = filter['precio_minimo'],
        #    pais__contains = filter['pais']
        #    )

        cursos = models.Curso.objects.all()

        if(cursos):
            serializer = serializers.CursoSerializer(cursos, many=True)
            return JSONResponse(serializer.data)
        else:
            response = {}
            response['data'] = 'course not found'
            return JSONResponse(response)

class CursoFilter(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None, categoria = False, nivel = False, pais = False, precio_max = False ):

        cursos = models.Curso.objects.filter(Q( categoria__nombre__contains = categoria ) |
                                             Q( nivel__nombre__contains = nivel ) |
                                             Q( pais__nombre__contains = pais ) |
                                             Q( precio__lte = precio_max ))

        if(cursos):
            serializer = serializers.CursoSerializer(cursos, many=True)
            return JSONResponse(serializer.data)
        else:
            response = {}
            response['msg'] = 'course not found'
            response['code'] = '404'
            return JSONResponse(response)
