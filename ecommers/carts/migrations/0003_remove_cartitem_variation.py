# Generated by Django 4.2.2 on 2023-06-24 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_cartitem_variation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='variation',
        ),
    ]
