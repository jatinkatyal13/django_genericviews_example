from django.urls import path

from .views import *

urlpatterns = [
	path('', Index.as_view(), name = 'index'),
	path('artists/', Artists.as_view(), name = 'artists'),
	path('artist/<slug:slug>', ArtistDetail.as_view(), name = 'artist_detail'),
	path('genres/', Genres.as_view(), name = 'genres'),
	path('genre/<slug:slug>', GenreDetail.as_view(), name = 'genre_detail'),
	path('song/<slug:slug>', Song.as_view(), name = 'song'),
]
