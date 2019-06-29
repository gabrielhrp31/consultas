# Generated by Django 2.0 on 2019-06-29 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consultations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultation',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='consultation',
            name='patient',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patients.Patient'),
        ),
    ]
