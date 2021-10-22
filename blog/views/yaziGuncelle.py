#from blog.forms import YaziGuncelleModelForm
#from django.contrib.auth.decorators import login_required
from blog.models import YazilarModel
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class YaziGuncelleUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('giris')
    template_name = 'pages/yaziGuncelle.html'
    fields = ('resim', 'baslik', 'icerik', 'kategoriler')

    def get_object(self):
        yazi = get_object_or_404(YazilarModel, slug = self.kwargs.get('slug'), yazar = self.request.user)
        return yazi

    def get_success_url(self):
        return reverse('detay', kwargs={'slug':self.get_object().slug})

"""
@login_required(login_url='/blog')
def yaziGuncelle(request, slug):
    
    yazi = get_object_or_404(YazilarModel, slug=slug, yazar=request.user)
    form = YaziGuncelleModelForm(request.POST or None, files=request.FILES or None, instance=yazi)
    if form.is_valid():
        form.save()
        return redirect('detay', slug=yazi.slug)

    return render(request, 'pages/yaziGuncelle.html', context={
        'form':form
    })
"""