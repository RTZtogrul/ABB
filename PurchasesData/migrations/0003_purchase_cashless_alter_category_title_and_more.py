# Generated by Django 4.1 on 2022-08-06 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PurchasesData', '0002_store_remove_purchase_store_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='cashless',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=50, unique=True, verbose_name='Category Title'),
        ),
        migrations.AlterField(
            model_name='user',
            name='FIN',
            field=models.CharField(default='FIN_UNKNOWN', max_length=7, unique=True, verbose_name='Fərdi İdentifikasiya Nömrəsi (FİN)'),
        ),
    ]
