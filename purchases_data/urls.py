from django.urls import path
from .views import home
from rest_framework import routers
from .views import PurchaseViewSet  

router = routers.DefaultRouter()
router.register('purchases', PurchaseViewSet)



urlpatterns = [
] + router.urls
