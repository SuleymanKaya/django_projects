# from blog.forms import yorumEkle
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import YazilarModel
from blog.forms import YorumEkleModelForm
from django.views import View
from django.contrib import messages
import logging

logger = logging.getLogger('yazi_okuma')

class DetayView(View):
    http_method_names = ['get', 'post']
    yorumEkle_form = YorumEkleModelForm

    def get(self, request, slug):
        yazi = get_object_or_404(YazilarModel, slug=slug)
        yorumlar = yazi.yorumlar.all()
        
        if request.user.is_authenticated:
            logger.info('yazi_okundu: ' + request.user.username)

        return render(request, 'pages/detay.html', context={
            'yazi': yazi,
            'yorumlar': yorumlar,
            'yorumEkle_form': self.yorumEkle_form()
    })

    def post(self, request, slug):
        yazi = get_object_or_404(YazilarModel, slug=slug)
        yorumEkle_form_post = self.yorumEkle_form(data=request.POST)

        if yorumEkle_form_post.is_valid():
            yorum = yorumEkle_form_post.save(commit=False)
            yorum.yazan = request.user
            yorum.yazi = yazi
            yorum.save()
            messages.success(request, "Yorumunuz Başarıyla Eklenmiştir")
        return redirect('detay', slug=yazi.slug)

"""
"1. ESKİ VERSİYON"
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

 "2. SELF. ÖRNEĞİ"
 # Write Python3 code here
 
class car():
     
    # init method or constructor
    def __init__(self, model, color):
        self.model = model
        self.color = color
         
    def show(self):
        print("Model is", self.model )
        print("color is", self.color )
         
# both objects have different self which
# contain their attributes
audi = car("audi a4", "blue")
ferrari = car("ferrari 488", "green")
 
audi.show()     # same output as car.show(audi)
ferrari.show()  # same output as car.show(ferrari)
 
# Behind the scene, in every instance method
# call, python sends the instances also with
# that method call like car.show(audi)   
"""