# Generated by Django 4.1 on 2024-01-23 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_alter_registration_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='RegNum',
        ),
    ]