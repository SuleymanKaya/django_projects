from django.shortcuts import render, redirect
from blog.forms import IletisimForm
from blog.models import IletisimModel

def iletisim(request):
    # data yerine initial yazılırsa alınan değerlerin validasyonu yapılmaz.
    form = IletisimForm(data={
        'email': 'xxxx@gmail.com',
        'isim_soyad': 'Adınızı Giriniz...',
        'mesaj': 'Mesajınızı Giriniz...'
    })
    if request.method == 'POST':
        form = IletisimForm(request.POST)
        if form.is_valid():
            form.save()
            #iletisim = IletisimModel()
            #iletisim.email = form.cleaned_data['email']
            #iletisim.isim_soyad = form.cleaned_data['isim_soyad']
            #iletisim.mesaj = form.cleaned_data['mesaj']
            #iletisim.save()
            return redirect('anasayfa')

    return render(request, 'pages/iletisim.html', context={
        'form': form
    })