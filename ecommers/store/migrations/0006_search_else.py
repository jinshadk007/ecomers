# Generated by Django 4.2.2 on 2023-06-24 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_delete_variation'),
    ]

    operations = [
        migrations.CreateModel(
            name='search_else',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='product')),
            ],
        ),
    ]
