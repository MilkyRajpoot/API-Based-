# Generated by Django 2.0 on 2020-02-01 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20200201_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipments',
            name='shipmentId',
            field=models.IntegerField(null=True),
        ),
    ]
