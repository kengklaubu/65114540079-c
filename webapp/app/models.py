from django.db import models

# Create your models here.
class Couses (models.Model):
    id = models.CharField( max_length=50)
    name = models.AutoField(max_length=55)

    def __str__(self):
        return super().__str__()

