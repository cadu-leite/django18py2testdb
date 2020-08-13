
from django import forms


from .models import Musica, Disco

# Create the form class.
class MusicForm(forms.Form):
    disco = forms.ChoiceField(choices=Disco.objects.all())

    class Meta:
        model = Musica
        fields = '__all__'


