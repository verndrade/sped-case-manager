from django.db import models

# Create your models here.
class Assignment(models.Model):
    course = models.CharField(max_length=200)
    assignment = models.CharField(max_length=200)
    assign_date = models.DateTimeField('date assigned')
    due_date = models.DateTimeField('date published')