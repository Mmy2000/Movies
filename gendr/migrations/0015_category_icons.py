# Generated by Django 4.2.4 on 2023-11-05 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gendr', '0014_all_like_delete_addtofavorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icons',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
