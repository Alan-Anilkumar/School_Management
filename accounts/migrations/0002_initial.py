# Generated by Django 5.1.2 on 2024-10-22 15:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.department'),
        ),
        migrations.AddField(
            model_name='staff',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.department'),
        ),
        migrations.AddField(
            model_name='student',
            name='grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='management.grade'),
        ),
    ]
