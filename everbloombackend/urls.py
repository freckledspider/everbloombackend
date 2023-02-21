from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from everbloominventory.views import InventoryViewSet


router = routers.DefaultRouter()
router.register(r'everbloominventory', InventoryViewSet) 


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]