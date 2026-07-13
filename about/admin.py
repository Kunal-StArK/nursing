from django.contrib import admin
from .models import Story
from .models import hopitalStats
# Register your models here.

class StoryAdmin(admin.ModelAdmin):
    list_display = ('story_title','story_discription')
    def has_add_permission(self, request):
        count = Story.objects.all().count()
        if count == 0 :
            return True
        return False


admin.site.register(Story,StoryAdmin)

class hopitalStatsAdmin(admin.ModelAdmin):
    list_display = ('year_of_service','expert_doctors','patients_treated','departments')
    def has_add_permission(self, request):
        count = hopitalStats.objects.all().count()
        if count == 0 :
            return True
        return False     


admin.site.register(hopitalStats,hopitalStatsAdmin)
