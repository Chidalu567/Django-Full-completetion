# Generated by Django 3.0.8 on 2020-10-24 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_auto_20201024_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=True),
        ),
    ]
