# Generated by Django 5.1.6 on 2025-04-08 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_appointmentform_iscomplete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointmentform',
            name='request_type',
            field=models.BooleanField(default=False),
        ),
    ]
