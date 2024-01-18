# en esta parte realizaremos el form que se visualiza en la parte de agregar un nuevo libro

from django import forms
from .models import Libro
class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'

