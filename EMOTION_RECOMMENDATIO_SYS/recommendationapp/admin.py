from django.contrib import admin
from .models import Song,Movie,Book,Error
# Register your models here.
admin.site.register(Song)
admin.site.register(Movie)
admin.site.register(Book)
admin.site.register(Error)
