from django.db import models

# Create your models here.

class Job(models.Model):

    image = models.ImageField(upload_to = "images/")
    summery = models.CharField(max_length=200)

    class Meta:
        db_table = 'jobs'

    def __str__(self) -> str:
        return f"{self.summery}"