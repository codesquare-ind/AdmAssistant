# Generated by Django 4.0.5 on 2022-06-20 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CallbackRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=35)),
                ('comment', models.CharField(blank=True, default='NA', max_length=850, null=True)),
                ('request_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
