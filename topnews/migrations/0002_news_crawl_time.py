# Generated by Django 2.2.2 on 2019-06-11 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topnews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='crawl_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
