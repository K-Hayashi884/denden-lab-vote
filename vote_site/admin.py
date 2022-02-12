from django.contrib import admin

from .models import Lab, Vote


class VoteAdmin(admin.ModelAdmin):
    list_display = ("email",)


class LabAdmin(admin.ModelAdmin):
    list_display = ("name", "belongs_to", "campus")


admin.site.register(Vote, VoteAdmin)
admin.site.register(Lab, LabAdmin)

# Register your models here.
