# Generated by Django 4.0.5 on 2022-07-07 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0030_location_added_by_sitesetting_fb_admin_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='added_by',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
