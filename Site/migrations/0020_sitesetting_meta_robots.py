# Generated by Django 4.0.5 on 2022-06-16 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0019_provider_is_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='meta_robots',
            field=models.CharField(default='index, follow', max_length=255),
        ),
    ]
