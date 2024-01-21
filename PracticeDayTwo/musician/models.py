from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class MusicianModel(models.Model):
    instrument_type=[
        ('Guitar','Guitar'),
        ('Tabla','Tabla'),
        ('Harmony','Harmony'),
        ('Behala','Behala'),
        ('Ektara','Ektara'),
    ]

    FirstName=models.CharField(max_length=100,unique=True)
    LastName=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    PhoneNumber=PhoneNumberField(default='+880')
    IntrumentType=models.CharField(max_length=100,choices=instrument_type)

    def __str__(self) -> str:
        return self.FirstName + ' ' + self.LastName
