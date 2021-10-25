#from django.shortcuts import render, redirect
#from blog.models import IletisimModel
from blog.forms import IletisimForm
from django.views.generic import FormView

class IletisimFormView(FormView):
    template_name = "pages/iletisim.html"
    form_class = IletisimForm
    success_url = "emailGonderildi"

    def form_valid(self, form):
        form.save()
        form.send_email(mesaj = form.cleaned_data.get('mesaj'))
        return super().form_valid(form)

"""
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
"""