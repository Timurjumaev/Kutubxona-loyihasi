from django import forms
from django.core.exceptions import ValidationError
from .models import Kitob


class StudentForm(forms.Form):
    i=forms.CharField(label='Ism')
    j=forms.CharField(label='Jins')
    bitiruvchi=forms.BooleanField()
    kitoblari_soni=forms.IntegerField()
    def clean_i(self):
        qiymat=self.cleaned_data.get('i')
        if not qiymat.endswith('bek') and not qiymat.endswith('jon'):
            raise ValidationError('Ism ozbekcha emas!')
        return qiymat
    def clean_kitoblari_soni(self):
        qiymat=self.cleaned_data.get('kitoblari_soni')
        if qiymat<0 or qiymat>5:
            raise ValidationError('Nol va besh oraligida kitob qoshing!')
        return qiymat

class KitobForm(forms.ModelForm):
    class Meta:
        model=Kitob
        fields=('nom', 'sahifa', 'janr', 'muallif')
