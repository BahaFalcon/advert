from rest_framework import serializers

from .models import Product, ProductCategory


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductByCategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='title')
    products = ProductSerializer(many=True)

    class Meta:
        model = ProductCategory
        fields = ('id', 'name', 'products')



