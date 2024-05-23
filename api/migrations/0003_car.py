# Generated by Django 5.0 on 2024-05-22 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('descryption', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
        ),
    ]
