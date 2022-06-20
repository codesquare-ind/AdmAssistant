# Generated by Django 4.0.5 on 2022-06-16 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0015_course_slug_provider_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallbackRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=35)),
                ('comment', models.CharField(blank=True, max_length=850, null=True)),
                ('request_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='sitesetting',
            name='fail_silently',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='sitesetting',
            name='host_password',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='sitesetting',
            name='host_user',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='sitesetting',
            name='smtp_host',
            field=models.CharField(blank=True, default='smtp.gmail.com', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sitesetting',
            name='smtp_port',
            field=models.CharField(blank=True, default=587, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='sitesetting',
            name='use_tls',
            field=models.BooleanField(default=True),
        ),
    ]
