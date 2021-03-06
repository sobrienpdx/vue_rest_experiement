# Generated by Django 2.0 on 2018-08-25 21:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2018, 8, 25, 21, 6, 23, 41264))),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct', models.FloatField()),
                ('incorrect', models.FloatField()),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2018, 8, 25, 21, 6, 23, 43877))),
            ],
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2018, 8, 25, 21, 6, 23, 42525))),
                ('cards', models.ManyToManyField(blank=True, related_name='sets', to='data_app.Card')),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='images',
            field=models.ManyToManyField(blank=True, related_name='cards', to='data_app.Image'),
        ),
    ]
