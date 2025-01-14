# Generated by Django 2.0 on 2019-07-17 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.TextField()),
                ('city', models.TextField()),
                ('street', models.TextField()),
                ('number', models.IntegerField()),
                ('district', models.TextField(default='Insira um Bairro')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='')),
                ('gender', models.NullBooleanField()),
                ('birth_date', models.DateField(null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.TextField()),
                ('RG', models.TextField()),
                ('CPF', models.TextField()),
                ('comments', models.TextField(null=True)),
                ('found_us_by', models.TextField(null=True)),
                ('address', models.ForeignKey(on_delete=models.SET(None), to='patients.Address')),
            ],
        ),
    ]
