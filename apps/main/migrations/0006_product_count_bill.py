# Generated by Django 3.1 on 2021-07-05 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210705_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='count_bill',
            field=models.PositiveIntegerField(default=0, verbose_name='Кол-во'),
        ),
    ]
