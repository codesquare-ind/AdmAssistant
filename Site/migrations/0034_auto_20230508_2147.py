# Generated by Django 3.2.9 on 2023-05-08 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0033_sitesetting_logo_url_dark'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='banner1_image',
            field=models.ImageField(blank=True, null=True, upload_to='Banners'),
        ),
        migrations.AddField(
            model_name='sitesetting',
            name='banner2_image',
            field=models.ImageField(blank=True, null=True, upload_to='Banners'),
        ),
        migrations.AddField(
            model_name='sitesetting',
            name='banner_image',
            field=models.ImageField(blank=True, null=True, upload_to='Banners'),
        ),
    ]
