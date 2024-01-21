from . models import AlbumModel
from django import forms 


class AlbumForm(forms.ModelForm):

    class Meta:
        model=AlbumModel
        fields='__all__'
        
        widgets={
            'ReleaseDate':forms.DateInput(attrs={'type':'date'})
        }
        labels={
            'ReleaseDate':'Release Date',
            'MusicianName':'Musician Name',
        }

