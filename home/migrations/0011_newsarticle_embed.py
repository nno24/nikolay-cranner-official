# Generated by Django 4.0.4 on 2022-10-16 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_newsarticle_section1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='embed',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
