from django import forms  
from .models import Estufa

class formCadastroEstufa(forms.ModelForm):
  class Meta:
    model = Estufa
    fields =('nome','temperatura','umidade')
