from django.db import models


# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title