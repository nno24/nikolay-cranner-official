# Generated by Django 4.0.4 on 2022-10-16 17:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_newsarticle_live'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='pubdate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]