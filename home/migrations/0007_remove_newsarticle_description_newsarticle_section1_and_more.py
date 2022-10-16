# Generated by Django 4.0.4 on 2022-10-16 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_newsarticle_media'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsarticle',
            name='description',
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='section1',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='section2',
            field=models.TextField(default=''),
        ),
    ]
