from django.shortcuts import render, get_object_or_404
from blog.forms import yorumEkle
from blog.models import YazilarModel
from blog.forms import YorumEkleModelForm

def detay(request, slug):
    yazi = get_object_or_404(YazilarModel, slug=slug)
    yorumlar = yazi.yorumlar.all()
    
    if request.method == 'POST':
        yorumEkle_form = YorumEkleModelForm(data=request.POST)
        if yorumEkle_form.is_valid():
            yorum = yorumEkle_form.save(commit=False)
            yorum.yazan = request.user
            yorum.yazi = yazi
            yorum.save()
    
    yorumEkle_form = YorumEkleModelForm()
    
    return render(request, 'pages/detay.html', context={
        'yazi': yazi,
        'yorumlar': yorumlar,
        'yorumEkle_form': yorumEkle_form
    })