from django.contrib import admin

from .models import Lab, User


class LabAdmin(admin.ModelAdmin):
    list_display = ("name", "belongs_to", "campus")


admin.site.register(User)
admin.site.register(Lab, LabAdmin)

# Register your models here.
