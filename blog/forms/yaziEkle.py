from django import forms
from blog.models import YazilarModel

class YaziEkleModelForm(forms.ModelForm):
    class Meta:
        model = YazilarModel
        # fields = ('resim', 'baslik', 'icerik', 'kategoriler') - exclude yerine bu kısımda kullanılabilir.
        exclude = ('slug', 'yazar')
