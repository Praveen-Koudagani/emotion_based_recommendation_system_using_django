"""EMOTION_RECOMMENDATIO_SYS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from django.conf.urls.static import static
from recommendationapp import views
urlpatterns = [
    path('', views.index ,name='index'),
    path('about', views.about ,name='about'),
    path('contact', views.contact,name='contact'),
    path('movies',views.movies,name='movies'),
    path('music',views.music,name="music"),
    path('cssdemo', views.cssdemo,name='cssdemo'),
    path('book',views.books,name='book'),
    path('pdf',views.pdf,name='pdf'),
    path('Error1',views.Error1,name="Error1")

    #path('recommendationapp/', include('recommendationapp.urls')),
]
