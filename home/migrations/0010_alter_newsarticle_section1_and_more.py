# Generated by Django 4.0.4 on 2022-10-16 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_newsarticle_pubdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='section1',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='section2',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
