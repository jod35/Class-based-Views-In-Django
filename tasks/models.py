from django.db import models

# Create your models here.

"""
class Task:
    date_created datetime
    id int
    name str
    description text
"""

class Task(models.Model):
    name = models.CharField(max_length=50)
    description =models.TextField()
    date_created =models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name