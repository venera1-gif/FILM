from django.contrib import admin

from movie.models import Genre,Actor,Movie

admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Movie)
