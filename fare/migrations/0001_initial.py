# Generated by Django 5.0.6 on 2024-05-17 16:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='coords',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='MapPopup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('route', models.CharField(max_length=255)),
                ('plate_no', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User_amount',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.FloatField(default=0.0)),
                ('last_transaction', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User_Transaction_history',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('transaction_amount', models.FloatField(default=0.0)),
                ('transaction_datetime', models.DateTimeField(auto_now_add=True)),
                ('pickup_point', models.FloatField(blank=True, null=True)),
                ('drop_point', models.FloatField(blank=True, null=True)),
                ('distance_covered', models.FloatField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
