
from .models import Serie, Categoria, Producto
from rest_framework import serializers

class SerieSerializer(serializers.ModelSerializer):
     class Meta:
         model = Serie
         fields = ('id', 'name', 'release_date', 'rating', 'category')
         
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'