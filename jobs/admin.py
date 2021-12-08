from django.contrib import admin

from jobs.models import Job

# Register your models here.

class JobModelAdmin(admin.ModelAdmin):
    list_display = ["summery", "image"]


admin.site.register(Job, JobModelAdmin)
