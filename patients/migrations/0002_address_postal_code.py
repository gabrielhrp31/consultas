# Generated by Django 2.0 on 2019-07-19 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='postal_code',
            field=models.TextField(default='00000-000'),
        ),
    ]
