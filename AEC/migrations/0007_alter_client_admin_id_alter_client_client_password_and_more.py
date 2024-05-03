# Generated by Django 5.0.1 on 2024-03-24 11:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AEC', '0006_alter_client_admin_id_alter_client_client_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='admin_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='AEC.admin'),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_password',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='client',
            name='emp_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='client',
            name='emp_role',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='client',
            name='employee_list',
            field=models.ManyToManyField(default=None, to='AEC.employee'),
        ),
        migrations.AlterField(
            model_name='client',
            name='req_id',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
    ]