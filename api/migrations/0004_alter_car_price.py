# Generated by Django 5.0 on 2024-05-22 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
