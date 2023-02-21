from django.db import models

# Create your models here.
#pet adoption project =>pet,vaccines-(many to many)

class Vaccines(models.Model):
    name=models.CharField(max_length=155,unique=True)
    
    def __str__(self):
        return self.name
    
class Pet(models.Model):
    GENDER_CHOICES=[
        ("M","Male"),
        ("F","Female")
    ]
    name=models.CharField(max_length=155)
    owner=models.CharField(max_length=155)
    submitted_on=models.DateTimeField()
    species=models.CharField(max_length=100)
    gender=models.CharField(max_length=2,choices=GENDER_CHOICES)
    age=models.IntegerField(blank=True)
    description=models.TextField(blank=True,null=True)
    Vaccines=models.ManyToManyField(Vaccines)
    
    def __str__(self):
        return self.name