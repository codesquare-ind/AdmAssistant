# Generated by Django 4.0.5 on 2022-07-07 10:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0028_sitesetting_fb_page_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='last_modified',
            field=models.DateField(default=datetime.date.today),
        ),
    ]