from .models import Cart
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = Cart
        # the fields that should be included in the serialized output
        fields = ['id', 'product', 'image', 'price', 'description', 'card']