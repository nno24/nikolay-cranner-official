# Generated by Django 4.0.4 on 2022-10-16 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_newsarticle_description_newsarticle_section1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='live',
            field=models.BooleanField(default=False),
        ),
    ]
