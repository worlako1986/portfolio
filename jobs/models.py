from os import name
from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=64)
    about = models.CharField(max_length=200)
    image = models.ImageField(upload_to = "images/")
    email = models.CharField(max_length=255, default="", blank=True)
    github_link = models.CharField(max_length=255, default="", blank=True)
    linkedin_link = models.CharField(max_length=255, default="", blank=True)
    youtube_link = models.CharField(max_length=255, default="", blank=True)


    class Meta:
        db_table = "persons"

    def __str__(self) -> str:
        return f"{self.name}"

class Job(models.Model):

    image = models.ImageField(upload_to = "images/")
    summery = models.CharField(max_length=200)
    description = models.TextField(default="")
    person = models.ForeignKey(Person, null=True, blank=True, related_name="person_jobs", verbose_name="Person related jobs", on_delete=models.CASCADE)

    class Meta:
        db_table = 'jobs'

    def __str__(self) -> str:
        return f"{self.summery}"

