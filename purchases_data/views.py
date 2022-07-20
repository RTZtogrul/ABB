from django.shortcuts import render


def home(request):
    return render(request, "purchases_data/purchase.html")
