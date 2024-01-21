from django.db import models
from musician.models import MusicianModel
# Create your models here.

class AlbumModel(models.Model):

    Rating=[
        ('1','One'),
        ('2','Two'),
        ('3','Three'),
        ('4','Four'),
        ('5','Five'),
    ]
    
    Name=models.CharField(max_length=200)
    Rating=models.CharField(max_length=10,choices=Rating)
    ReleaseDate=models.DateField()
    MusicianName=models.ForeignKey(to=MusicianModel,on_delete=models.CASCADE,related_name='musician')

