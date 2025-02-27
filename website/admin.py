from django.contrib import admin
from website import models
# Register your models here.

# admin.site.register(models.TaskType)

class TaskAdmin(admin.ModelAdmin):
	list_display=("name","created_date","status","expiry_date","priority")
admin.site.register(models.Task,TaskAdmin)