# Generated by Django 2.0 on 2019-07-06 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultations', '0010_auto_20190702_1848'),
        ('financier', '0002_patientfinancial_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientfinancial',
            name='consultation',
            field=models.ForeignKey(null=True, on_delete=models.SET(None), to='consultations.Consultation'),
        ),
    ]
