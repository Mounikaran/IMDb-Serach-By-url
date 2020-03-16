from django.shortcuts import render
from re import findall

from django.http import JsonResponse

# imdb 
from imdb import IMDb
#from imdb.helpers import get_byURL

from .models import Movie
# Create your views here.

def search(request):
	url = request.POST.get('imdb_url')
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
		movie_obj = Movie.objects.filter(title=title).values()
		mvie = list(movie_obj)
		return JsonResponse(mvie, safe=False)
	
	return render(request, 'search.html', {})
