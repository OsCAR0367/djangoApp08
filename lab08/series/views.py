from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics 

from .models import Serie, Categoria, Producto
from .serializers import CategoriaSerializer, ProductoSerializer, SerieSerializer

class IndexView(APIView):
    def get(self, request):
        context = {'mensaje': 'servidor activo'}
        return Response(context)

class SeriesView(generics.ListCreateAPIView): 
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer

class SerieDetailView(APIView):
    def get(self, request, serie_id):
        dataSerie = Serie.objects.get(pk=serie_id)
        serSerie = SerieSerializer(dataSerie)
        return Response(serSerie.data)

    def put(self, request, serie_id):
        dataSerie = Serie.objects.get(pk=serie_id)
        serSerie = SerieSerializer(dataSerie, data=request.data)
        serSerie.is_valid(raise_exception=True)
        serSerie.save()
        return Response(serSerie.data)

    def delete(self, request, serie_id):
        dataSerie = Serie.objects.get(pk=serie_id)
        serSerie = SerieSerializer(dataSerie)
        dataSerie.delete()
        return Response(serSerie.data)

class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
