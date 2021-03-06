# Generated by Django 3.2 on 2021-05-17 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PayByLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=5)),
                ('amount', models.IntegerField(max_length=100)),
                ('description', models.TextField(max_length=30)),
                ('bank', models.CharField(max_length=20)),
            ],
        ),
    ]
