# Generated by Django 5.0.6 on 2024-05-17 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fare', '0004_alter_user_amount_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MapPopup',
        ),
        migrations.DeleteModel(
            name='RealTimecoords',
        ),
    ]
