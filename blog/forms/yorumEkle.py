from django import forms
from django.forms import fields
from django.forms.models import ModelForm
from blog.models import YorumModel

class YorumEkleModelForm(forms.ModelForm):
    class Meta:
        model = YorumModel
        fields = ('yorum', )
