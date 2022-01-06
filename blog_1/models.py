from django.db import models

# Create your models here.


class Blog_Table(models.Model):
    Title=models.CharField(max_length=100)
    description=models.TextField()
    def __str__(self):
        return self.Title +' '+self.description
