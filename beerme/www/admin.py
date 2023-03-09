from django.contrib import admin

from .models import Team, Driver, Track, Race, Person, Bet, Tv

# Register your models here.


class RaceAdmin(admin.ModelAdmin):
    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == "title":
    #         kwargs["queryset"] = Foo.objects.filter(title__isnull=False)
    #     return super(RaceAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
    list_filter = ["tv_id"]
    list_display = ["race_date", "track_id", "tv_id", "track_web_site"]
    list_display_links = ["track_id", "track_web_site"]


class BetAdmin(admin.ModelAdmin):
    list_display = [
        "beer",
        "person_id",
        "race_id",
        "driver_id",
        "finish",
    ]
    ordering = ["race_id"]


class DriverAdmin(admin.ModelAdmin):
    list_display = ["name", "web_site"]


class TeamAdmin(admin.ModelAdmin):
    list_display = ["name", "web_site"]
    # list_display_links = ["web_site"]


class TrackAdmin(admin.ModelAdmin):
    list_display = ["name", "web_site"]
    ordering = ["name"]


admin.site.register(Team, TeamAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Track, TrackAdmin)
admin.site.register(Race, RaceAdmin)
admin.site.register(Person)
admin.site.register(Tv)
admin.site.register(Bet, BetAdmin)
