# Generated by Django 4.0.5 on 2022-06-20 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0025_alter_callbackrequest_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CallbackRequest',
        ),
    ]
