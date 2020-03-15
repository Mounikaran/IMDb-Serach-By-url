from django.db import models
from django_mysql.models import ListCharField
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Movie(models.Model):
	title = models.CharField(max_length=50)
	year = models.CharField(max_length=10)
	plot = models.CharField(max_length=400, default="")
	rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
	stars = ListCharField(
		base_field = models.CharField(max_length=35),
		size = 100,
		max_length = (100 * 50)
		)
	writer = ListCharField(
		base_field = models.CharField(max_length=35),
		size = 20,
		max_length = (20 * 50)
		)
	director = ListCharField(
		base_field = models.CharField(max_length=35),
		size = 15,
		max_length = (15 * 50)
		)

	def __str__(self):
		return self.title
