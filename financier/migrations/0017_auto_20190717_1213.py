# Generated by Django 2.0 on 2019-07-17 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('financier', '0016_auto_20190715_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cost',
            name='plots',
        ),
        migrations.RemoveField(
            model_name='patientfinancial',
            name='status',
        ),
        migrations.AddField(
            model_name='plots',
            name='cost',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='financier.Cost'),
        ),
        migrations.AddField(
            model_name='plots',
            name='type',
            field=models.IntegerField(default=2),
        ),
    ]