# Generated by Django 4.0 on 2023-09-13 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_company_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewer',
            name='date',
            field=models.CharField(max_length=200),
        ),
    ]