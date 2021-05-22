# Generated by Django 3.1.7 on 2021-04-12 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendationapp', '0002_auto_20210412_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='artist',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='music',
            name='audio_file',
            field=models.FileField(blank=True, null=True, upload_to='songs_dir'),
        ),
        migrations.AlterField(
            model_name='music',
            name='image',
            field=models.ImageField(upload_to='songs_images'),
        ),
        migrations.AlterField(
            model_name='music',
            name='title',
            field=models.TextField(max_length=100),
        ),
    ]
