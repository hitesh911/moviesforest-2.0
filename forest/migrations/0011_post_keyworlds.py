# Generated by Django 3.2.1 on 2021-06-12 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forest', '0010_post_ips'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='keyworlds',
            field=models.TextField(default='download now'),
        ),
    ]
