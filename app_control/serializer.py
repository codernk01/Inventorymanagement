from rest_framework import serializers
from .models import Inventory,Factory

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'

class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = '__all__'