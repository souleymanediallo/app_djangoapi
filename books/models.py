from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to="books", null=True, blank=True)
    published = models.DateField(blank=True, null=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title