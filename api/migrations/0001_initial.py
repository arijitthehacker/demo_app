# Generated by Django 5.0.6 on 2024-05-16 06:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField(max_length=100)),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
                'db_table': 'UserModel',
            },
        ),
        migrations.CreateModel(
            name='SchoolModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usermodel')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
                'db_table': 'SchoolModel',
            },
        ),
    ]
