# Generated by Django 3.1.7 on 2021-04-25 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendationapp', '0005_auto_20210414_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=150)),
                ('artists', models.TextField(max_length=400)),
                ('image', models.ImageField(upload_to='media/movie_images')),
                ('movie_link', models.CharField(max_length=2000)),
                ('mood', models.TextField(max_length=10)),
            ],
        ),
    ]