# Generated by Django 5.0.1 on 2024-03-24 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AEC', '0009_rename_req_id_client_client_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='client_id',
            new_name='req_id',
        ),
    ]
