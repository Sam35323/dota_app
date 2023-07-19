from django.contrib import admin
from .models import Hero, Position, TopClass

class HeroAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'disc', 'bio')
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Hero, HeroAdmin)


class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'position_name',)
    prepopulated_fields = {"slug": ("position_name",)}


admin.site.register(Position, PositionAdmin)

admin.site.register(TopClass)
