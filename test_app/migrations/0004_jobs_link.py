# Generated by Django 5.1 on 2024-08-16 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0003_jobs'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='link',
            field=models.URLField(default=None, max_length=1000),
        ),
    ]
