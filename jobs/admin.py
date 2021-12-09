from django.contrib import admin

from jobs.models import Job, Person

# Register your models here.

class JobModelAdmin(admin.ModelAdmin):
    list_display = ["person","summery", "image"]

class PersonModelAdmin(admin.ModelAdmin):
    list_display = ["name", "about", "image"]

admin.site.register(Job, JobModelAdmin)
admin.site.register(Person, PersonModelAdmin)
