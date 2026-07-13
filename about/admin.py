from django.contrib import admin
from .models import Story
from .models import hopitalStats
# Register your models here.

class StoryAdmin(admin.ModelAdmin):
    list_display = ('story_title','story_discription')


admin.site.register(Story,StoryAdmin)

class hopitalStatsAdmin(admin.ModelAdmin):
    list_display = ('year_of_service','expert_doctors','patients_treated','departments')


admin.site.register(hopitalStats,hopitalStatsAdmin)
