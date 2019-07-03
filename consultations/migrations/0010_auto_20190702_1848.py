# Generated by Django 2.0 on 2019-07-02 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultations', '0009_auto_20190702_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultation',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='consultation',
            name='payment',
            field=models.BooleanField(default=False),
        ),
    ]