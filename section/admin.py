from django.contrib import admin
from .models import Achievement, Project, Activity, Team, Announcement

# Register your models here.
admin.site.register(Achievement)
admin.site.register(Project)
admin.site.register(Activity)
admin.site.register(Team)
admin.site.register(Announcement)