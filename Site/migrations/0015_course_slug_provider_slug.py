# Generated by Django 4.0.5 on 2022-06-16 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0014_faq'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(blank=True, max_length=450, null=True),
        ),
        migrations.AddField(
            model_name='provider',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]
