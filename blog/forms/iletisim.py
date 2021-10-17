from django import forms
from django.forms import fields
from blog.models import IletisimModel

#class IletisimForm(forms.Form):
    #email = forms.EmailField(label="Mail Adresi", max_length=200)
    #isim_soyad = forms.CharField(label="İsim Soyad", max_length=100)
    #mesaj = forms.CharField(label="Mesajınız", widget=forms.Textarea) - crispy kullanımında yeterli
    #mesaj = forms.CharField(label="Mesajınız", widget=forms.Textarea(attrs={
    #    'class': 'form-control'
    #}))

class IletisimForm(forms.ModelForm):
    class Meta:
        model = IletisimModel
        fields = ('email', 'isim_soyad', 'mesaj' )
