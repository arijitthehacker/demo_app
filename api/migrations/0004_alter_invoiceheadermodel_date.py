# Generated by Django 5.0.6 on 2024-05-16 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_invoiceheadermodel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceheadermodel',
            name='date',
            field=models.DateField(auto_created=True, auto_now_add=True),
        ),
    ]
