from django.contrib import admin

from .models import Team, Driver, Track, Race, Person, Bet, Tv

# Register your models here.


class BetAdmin(admin.ModelAdmin):
    list_display = [
        "beer",
        "person_id",
        "race_id",
        "driver_id",
        "finish",
    ]


admin.site.register(Team)
admin.site.register(Driver)
admin.site.register(Track)
admin.site.register(Race)
admin.site.register(Person)
admin.site.register(Tv)
admin.site.register(Bet, BetAdmin)
