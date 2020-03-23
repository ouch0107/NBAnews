# Generated by Django 2.2.2 on 2019-06-11 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(max_length=100)),
                ('pre_img_link', models.URLField(max_length=100)),
                ('title', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=10)),
                ('preview', models.CharField(max_length=100)),
                ('img_link', models.URLField(max_length=100)),
                ('paragraph', models.CharField(max_length=200)),
            ],
        ),
    ]