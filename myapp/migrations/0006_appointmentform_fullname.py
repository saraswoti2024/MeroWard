# Generated by Django 5.1.6 on 2025-04-08 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_appointmentform_isschedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmentform',
            name='fullname',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
