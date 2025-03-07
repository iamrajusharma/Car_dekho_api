# Generated by Django 5.1.6 on 2025-02-15 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardekho_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carlist',
            name='chassinumber',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='carlist',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
    ]
