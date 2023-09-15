# Generated by Django 4.2.4 on 2023-09-15 13:51

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('gendr', '0008_category2_all_category2'),
    ]

    operations = [
        migrations.AddField(
            model_name='all',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='tags'),
        ),
    ]
