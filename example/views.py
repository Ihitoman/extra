from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework import status


from django.shortcuts import get_object_or_404
from django.http import Http404

import time

#IsAuthenticated


from example.models import Actividad
from example.models import Cosa


from example.serializer import ActividadSerializer
from example.serializer import CosaSerializer


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

#vistas de extra





class ActividadList(APIView):
    
    def get(self, request, format=None):
        queryset = Actividad.objects.all()
        serializer = ActividadSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        Actividaad = Actividad.objects.create(
            name = request.data['name'],
            date = request.data['date'],
            hour = request.data['hour']
        )
        Actividaad.save()
        return Response("simon we")



class ActividadDetail(APIView):
    def get_object(self, id):
        try:
            return Actividad.objects.get(pk=id)
        except Actividad.DoesNotExist:
            return False
    
    def get(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = ActividadSerializer(example)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Actividad.objects.get(pk=id).delete()
        return Response("ok")
    
    def put(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = ActividadSerializer(example, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)





class CosaListA(APIView):
    
    def get(self, request, id, format=None):
        queryset = Cosa.objects.filter(actividad_id=id)
        serializer = CosaSerializer(queryset, many=True)
        return Response(serializer.data)
    

class CosaList(APIView):
    def post(self, request, format=None):
        serializer = CosaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



class CosaDetail(APIView):
    def get_object(self, id):
        try:
            return Actividad.objects.get(pk=id)
        except Actividad.DoesNotExist:
            return False
    
    def get(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = ActividadSerializer(example)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Actividad.objects.get(pk=id).delete()
        return Response("ok")
    
    def put(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = ActividadSerializer(example, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
