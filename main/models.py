from django.db import models

from django.template.defaultfilters import slugify

# Create your models here.

class Artist (models.Model):
	name = models.CharField(max_length = 200)
	slug = models.SlugField()

	class Meta:
		ordering = ['name']

	def __str__ (self):
		return self.name

	def save(self, *args, **kwargs):
		if self.slug == "" or not self.slug:
			self.slug = slugify(self.name)
		super(Artist, self).save(*args, **kwargs)

class Genre (models.Model):
	name = models.CharField(max_length = 200)
	slug = models.SlugField()

	class Meta:
		ordering = ['name']

	def __str__ (self):
		return self.name

	def save(self, *args, **kwargs):
		if self.slug == "" or not self.slug:
			self.slug = slugify(self.name)
		super(Genre, self).save(*args, **kwargs)

class Song (models.Model):
	name = models.CharField(max_length = 200)
	slug = models.SlugField()
	link = models.URLField()
	artist = models.ForeignKey(Artist, on_delete = models.CASCADE)
	genre = models.ManyToManyField(Genre)

	class Meta:
		ordering = ['name']

	def __str__ (self):
		return self.name

	def save(self, *args, **kwargs):
		if self.slug == "" or not self.slug:
			self.slug = slugify(self.name)
		super(Song, self).save(*args, **kwargs)
