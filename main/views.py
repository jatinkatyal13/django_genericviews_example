from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import *

# Create your views here.

class Index(TemplateView):
	template_name = 'main/index.html'

class Artists(ListView):
	model = Artist
	template_name = 'main/artist_list.html'

class ArtistDetail(DetailView):
	model = Artist
	template_name = 'main/artist_detail.html'

class Genres(ListView):
	model = Genre
	template_name = 'main/genre_list.html'

class GenreDetail(DetailView):
	model = Genre
	template_name = 'main/genre_detail.html'

class Song(DetailView):
	model = Song
	template_name = 'main/song.html'
