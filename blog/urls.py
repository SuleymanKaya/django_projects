from django.conf.urls import url
from django.urls import path
from blog.views import IletisimFormView, anasayfa, KategoriListView, yazilarim, DetayView, YaziEkleCreateView, YaziGuncelleUpdateView, YaziSilDeleteView, yorumSil
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    #path('iletisim', iletisim, name='iletisim'),
    #path('yaziEkle', yaziEkle, name='yaziEkle'),
    #path('yaziGuncelle/<slug:slug>', yaziGuncelle, name='yaziGuncelle'),
    #path('yaziSil/<slug:slug>', yaziSil, name='yaziSil'), 
    path("", anasayfa, name='anasayfa'),
    path('iletisim', IletisimFormView.as_view(), name='iletisim'),
    path('kategori/<slug:kategoriSlug>', KategoriListView.as_view(), name='kategori'),
    path('yazilarim', yazilarim, name='yazilarim'),
    path('detay/<slug:slug>', DetayView.as_view(), name='detay'),
    path('yaziEkle', YaziEkleCreateView.as_view(), name='yaziEkle'),
    path('yaziGuncelle/<slug:slug>', YaziGuncelleUpdateView.as_view(), name='yaziGuncelle'),
    path('yaziSil/<slug:slug>',YaziSilDeleteView.as_view(), name='yaziSil'),
    path('yorumSil/<int:id>', yorumSil, name='yorumSil'),
    path('hakkimda', TemplateView.as_view(template_name = 'pages/hakkimda.html'), name='hakkimda'),
    path('googleYonlendir', RedirectView.as_view( url='https://www.google.com'), name='googleYonlendir'),
    path('emailGonderildi', TemplateView.as_view(template_name = 'pages/emailGonderildi.html'), name='emailGonderildi')
]
