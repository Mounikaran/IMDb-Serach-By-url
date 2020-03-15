from django.shortcuts import render
from re import findall

# imdb 
from imdb import IMDb
#from imdb.helpers import get_byURL

from .models import Movie
# Create your views here.

def search(request):
	url = request.POST.get('imdb_url')
	found = False
	cover = None
	if url:
		ID = findall(r'\d+', url)[0]
		imdb_obj = IMDb()
		MOVIE = imdb_obj.get_movie(ID)
		title = MOVIE['title']
		plot = MOVIE['plot'][0]
		director = MOVIE['director']
		writer = MOVIE['writer']
		rating = MOVIE['rating']
		year = MOVIE['year']
		stars = MOVIE['cast']
		cover = MOVIE['cover url']

		try:
			exist = Movie.objects.get(title=title)
		except Movie.DoesNotExist:
			exist = None
		if not exist:
			movie = Movie()
			movie.title = title
			movie.plot = plot
			movie.rating = rating
			movie.director = director
			movie.writer = writer
			movie.stars = stars
			movie.year = year
			movie.save()
		searched_movie = Movie.objects.get(title=title)
		found = True
	else:
		print("Nothing typed")
		searched_movie = ['Nothing', 'Found']
	return render(request, 'search.html', {
		'found':found,
		'movie':searched_movie,
		'cover':cover,
		})
