# Generated by Django 3.2.12 on 2023-10-02 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SettingsPreview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('previewId', models.IntegerField()),
                ('HideReviewsWithoutComments', models.BooleanField()),
                ('HideRatingText', models.BooleanField()),
                ('ShowReviewersPhoto', models.BooleanField()),
                ('ShowReviewersName', models.BooleanField()),
                ('ShowViewAllReviewsLink', models.BooleanField()),
                ('ShowWriteReviewButton', models.BooleanField()),
                ('AutoPlay', models.BooleanField()),
                ('EnableHyperLink', models.BooleanField()),
                ('minratings', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=100)),
                ('dateformat', models.CharField(choices=[('my', 'Month-Year'), ('ymd', 'Year-Month-Day'), ('mdy', 'Month-Day-Year'), ('hide', 'Hide')], max_length=100)),
                ('align', models.CharField(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], max_length=100)),
                ('theme', models.CharField(choices=[('light', 'Light'), ('dark', 'Dark'), ('transparent', 'Transparent'), ('custom', 'Custom')], max_length=100)),
                ('cardbody', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=100)),
                ('cardbg', models.CharField(max_length=100)),
            ],
        ),
    ]
