from django.shortcuts import render
from .serializer import PurchaseSerializer
from .models import Purchase 
from rest_framework import viewsets

def home(request):
    return render(request, "purchases_data/purchase.html")


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
