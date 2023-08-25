# Generated by Django 4.2.4 on 2023-08-24 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('what_we_do', models.TextField(max_length=5000)),
                ('our_mission', models.TextField(max_length=5000)),
                ('our_gaols', models.TextField(max_length=5000)),
                ('image', models.ImageField(upload_to='about/')),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=3000)),
            ],
        ),
    ]
