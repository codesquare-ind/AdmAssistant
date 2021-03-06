# Generated by Django 4.0.5 on 2022-06-16 15:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0016_callbackrequest_sitesetting_fail_silently_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_type', models.CharField(choices=[('Standard', 'Standard'), ('In-Writing', 'In-Writing'), ('Audio', 'Audio'), ('Video', 'Video')], max_length=50)),
                ('name', models.CharField(max_length=150)),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)])),
                ('feedback', models.CharField(blank=True, help_text='for Standard type, simple message', max_length=850, null=True)),
                ('feedback_path', models.ImageField(blank=True, help_text='for in-writing image/photo', null=True, upload_to='FeedBacks/img')),
                ('feedback_url', models.URLField(blank=True, help_text='for youtube/other video/audio link', null=True)),
                ('feedback_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
