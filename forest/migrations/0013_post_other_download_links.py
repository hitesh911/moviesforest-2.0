# Generated by Django 3.2.1 on 2021-07-17 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forest', '0012_rename_keyworlds_post_keywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='other_download_links',
            field=models.TextField(default=' {"480":"https://480", "720":"https://720","1080":"https://1080"}'),
        ),
    ]