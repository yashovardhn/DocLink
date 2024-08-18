# Generated by Django 5.0.7 on 2024-08-18 15:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_prescription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='prescription_file',
        ),
        migrations.AlterField(
            model_name='prescription',
            name='appointment',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.appointment'),
        ),
    ]
