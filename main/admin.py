from django.contrib import admin

from .models import *

# Register your models here.

class SlugExclude(admin.ModelAdmin):
	exclude = ('slug',)

admin.site.register(Artist, SlugExclude)
admin.site.register(Genre, SlugExclude)
admin.site.register(Song, SlugExclude)
