# Generated by Django 4.2.4 on 2023-08-27 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gendr', '0006_remove_all_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='all',
            name='image2',
            field=models.ImageField(default=1, upload_to='all/'),
            preserve_default=False,
        ),
    ]
