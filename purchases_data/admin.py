from django.contrib import admin
from .models import Person, Category, Product, Purchase, PurchaseProduct

admin.site.register(Person)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Purchase)
admin.site.register(PurchaseProduct)
