# Generated by Django 3.1.2 on 2020-10-22 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_confirmstring'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='has_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
