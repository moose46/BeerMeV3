from django.contrib import admin

from .models import Team, Driver, Track, Race, Person, Bet, Tv

# Register your models here.


class RaceAdmin(admin.ModelAdmin):
    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == "title":
    #         kwargs["queryset"] = Foo.objects.filter(title__isnull=False)
    #     return super(RaceAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
    list_filter = ["tv_id"]


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
admin.site.register(Race, RaceAdmin)
admin.site.register(Person)
admin.site.register(Tv)
admin.site.register(Bet, BetAdmin)
