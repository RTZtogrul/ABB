from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True, unique=True)
    mobile = PhoneNumberField(unique=True)
    birthdate = models.DateField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ' ' + self.surname


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
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
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
