from .models import Inventory
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CartSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.AllowAny] 