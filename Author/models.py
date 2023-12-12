from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length = 40)
    born_on = models.DateField()
    psevdonim = models.CharField(max_length = 40)
    

    def __str__(self) -> str:
        return self.name