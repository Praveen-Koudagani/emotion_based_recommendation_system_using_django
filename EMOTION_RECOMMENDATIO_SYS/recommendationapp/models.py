from django.db import models

# Create your models here.

class Song(models.Model):
    title= models.TextField(max_length=100)
    artist= models.TextField(max_length=100)
    image= models.ImageField(upload_to='media/songs_images')
    audio_file = models.FileField(upload_to='media/songs_dir')
    audio_link = models.CharField(max_length=200,blank=True,null=True)
    mood=models.TextField(max_length=10)

    def __str__(self):
        return self.title
class Movie(models.Model):
    name=models.TextField(max_length=150)
    artists=models.TextField(max_length=400)
    image=models.ImageField(upload_to="media/movie_images")
    movie_link=models.URLField(max_length=2000)
    mood=models.TextField(max_length=10)
    def __str__(self):
        return self.name

class Book(models.Model):
    name=models.TextField(max_length=150)
    author=models.TextField(max_length=400)
    image=models.ImageField(upload_to="media/book_images")
    book_link=models.URLField(max_length=2000)
    book_file = models.FileField(upload_to='media/books_dir')
    mood=models.TextField(max_length=10)
    def __str__(self):
        return self.name