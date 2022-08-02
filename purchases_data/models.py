from django.db import models


class Person(models.Model):
    FIN = models.CharField(verbose_name="Fin", max_length=7, default='FIN_UNKNOWN')

    def __str__(self):
        return self.FIN


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title


class Purchase(models.Model):
    user = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    store_name = models.CharField(max_length=50)
    store_address = models.CharField(max_length=150)
    datetime = models.DateTimeField()
    total_bill = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return str(self.user) + '-' + self.store_name + '-' + str(self.datetime)


class PurchaseProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    purchase = models.ForeignKey(Purchase, on_delete=models.DO_NOTHING)
    quantity = models.FloatField()

    def __str__(self):
        return str(self.purchase) + '-' + str(self.product)
