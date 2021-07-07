# Generated by Django 3.1 on 2021-07-07 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210705_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10, verbose_name='Цена товара'),
            preserve_default=False,
        ),
    ]