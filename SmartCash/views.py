from django.shortcuts import render


def home(request):
    return render(request, r"purchases_data/purchase.html")
