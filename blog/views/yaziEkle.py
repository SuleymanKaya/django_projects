#from blog.forms import YaziEkleModelForm
#from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from blog.models.yazi import YazilarModel
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class YaziEkleCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('giris')
    template_name = 'pages/yaziEkle.html'
    model = YazilarModel
    fields = ('resim', 'baslik', 'icerik', 'kategoriler')
    #exclude değişkeni aktif değil !!

    def form_valid(self, form):
        if form.is_valid():
            yazi = form.save(commit=False)
            yazi.yazar = self.request.user
            yazi.save()
            form.save_m2m() 
        return redirect('detay', slug = yazi.slug)

"""
@login_required(login_url='/blog')
def yaziEkle(request):

    form = YaziEkleModelForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        yazi = form.save(commit=False)
        yazi.yazar = request.user
        yazi.save()
        form.save_m2m()
        return redirect('detay', slug = yazi.slug)

    return render(request, 'pages/yaziEkle.html', context={
        'form':form
    })
"""