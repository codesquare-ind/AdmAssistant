# Generated by Django 4.0.5 on 2022-06-13 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0012_sitesetting_ga_code_sitesetting_go_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='flag_url',
            field=models.URLField(blank=True, default='', max_length=255, null=True),
        ),
    ]
