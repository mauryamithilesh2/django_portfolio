# Generated by Django 5.1.7 on 2025-03-19 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='contact',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
