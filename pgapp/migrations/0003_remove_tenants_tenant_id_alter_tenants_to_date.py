# Generated by Django 4.0.5 on 2022-06-19 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pgapp', '0002_alter_tenants_advance_alter_tenants_phno_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tenants',
            name='tenant_id',
        ),
        migrations.AlterField(
            model_name='tenants',
            name='to_date',
            field=models.DateField(default=None),
        ),
    ]
