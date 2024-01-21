from . models import MusicianModel

from django import forms

class MusicianForm(forms.ModelForm):
    class Meta:
        model=MusicianModel
        fields='__all__'

        labels={
            'FirstName':'First Name',
            'LastName':'Last Name',
            'PhoneNumber':'Phone Number',
            'IntrumentType':'Intrument Type',

        }

    