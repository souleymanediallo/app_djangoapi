from django.db import models


class BookNumber(models.Model):
    isbn_10 = models.CharField(max_length=10, blank=True, null=True)
    isbn_13 = models.CharField(max_length=13, blank=True, null=True)

    def __str__(self):
        return str(self.isbn_10)


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to="books", null=True, blank=True)
    published = models.DateField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    number = models.OneToOneField(BookNumber, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Character(models.Model):
    name = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='characters')

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='authors')