# Generated by Django 4.0 on 2023-09-13 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='reviewer',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]