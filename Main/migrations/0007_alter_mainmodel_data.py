# Generated by Django 4.2.15 on 2024-11-24 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0006_alter_mainmodel_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainmodel',
            name='data',
            field=models.TextField(blank=True, null=True),
        ),
    ]
