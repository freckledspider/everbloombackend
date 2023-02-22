from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from everbloomcart.views import CartViewSet


router = routers.DefaultRouter()
router.register(r'everbloomcart', CartViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]