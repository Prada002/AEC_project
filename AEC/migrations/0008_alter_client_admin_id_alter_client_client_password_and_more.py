# Generated by Django 5.0.1 on 2024-03-24 11:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AEC', '0007_alter_client_admin_id_alter_client_client_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='admin_id',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='AEC.admin'),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_password',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='emp_count',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='emp_role',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
