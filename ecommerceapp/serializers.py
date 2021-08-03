from rest_framework import serializers
from . models import Category, Product

#serializer classes 

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            "id",
            "title"
        )
        model = Category


class ProductSerializer(serializers.ModelSerializer):

    class Meta: 
        fields = (
            'id',
            'product_tag',
            'title',
            'price',
            'imageUrl',
            'in_stock',
            'status',
            'description',
            'date_created',
        )
        model = Product