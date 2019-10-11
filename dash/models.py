from django.db import models

# Create your models here.
class Questions(models.Model):
    question = models.CharField(max_length=200, primary_key=True)
    optionA = models.CharField(max_length=200)
    optionB = models.CharField(max_length=200)
    optionC = models.CharField(max_length=200)
    optionD = models.CharField(max_length=200)
    answer = models.PositiveSmallIntegerField()
    marks = models.PositiveSmallIntegerField()
