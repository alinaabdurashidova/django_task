from django.db import models
from Author.models import Author

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length = 40)
    created_at = models.DateField()
    genre = models.CharField(max_length = 40)
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE,
        related_name='books'
    )
    

    def __str__(self) -> str:
        return self.title