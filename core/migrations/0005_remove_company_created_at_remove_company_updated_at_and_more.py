# Generated by Django 4.0 on 2023-09-13 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_company_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='company',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='reviewer',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='reviewer',
            name='updated_at',
        ),
    ]
