# Generated by Django 4.2.2 on 2023-06-12 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_product_available'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='available',
            new_name='is_available',
        ),
    ]
