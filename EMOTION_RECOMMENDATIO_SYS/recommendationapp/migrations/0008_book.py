# Generated by Django 3.1.7 on 2021-05-18 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendationapp', '0007_auto_20210426_0123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=150)),
                ('author', models.TextField(max_length=400)),
                ('image', models.ImageField(upload_to='media/book_images')),
                ('book_link', models.URLField(max_length=2000)),
                ('book_file', models.FileField(upload_to='media/books_dir')),
                ('mood', models.TextField(max_length=10)),
            ],
        ),
    ]