from django.contrib import admin
from gameshop.models import GameProducer, Game

class GamesAdmin(admin.ModelAdmin):
    list_display = ('name', 'producer', 'value', 'bio', 'year')
    search_fields = ('name', 'producer')

admin.site.register(Game, GamesAdmin)

class GamesProducerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(GameProducer, GamesProducerAdmin)
