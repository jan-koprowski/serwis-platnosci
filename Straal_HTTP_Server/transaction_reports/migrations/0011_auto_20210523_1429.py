# Generated by Django 3.2 on 2021-05-23 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction_reports', '0010_auto_20210523_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentmodel',
            name='amount',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='paymentmodel',
            name='customer_id',
            field=models.PositiveIntegerField(blank='True'),
        ),
    ]
