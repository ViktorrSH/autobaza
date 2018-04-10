from django.db import models

# Create your models here.

class car(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    def __str__(self):
       return '<name: {}, ID: {}>'.format(self.name, self.id)


