# Generated by Django 5.1.5 on 2025-01-19 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.CharField(default='bbsr', max_length=70),
            preserve_default=False,
        ),
    ]
