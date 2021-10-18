from django.urls import path
from blog.views import iletisim, anasayfa, kategori, yazilarim, detay, yaziEkle, yaziGuncelle, yaziSil, yorumSil

urlpatterns = [
    path("", anasayfa, name='anasayfa'),
    path('iletisim', iletisim, name='iletisim'),
    path('kategori/<slug:kategoriSlug>', kategori, name='kategori'),
    path('yazilarim', yazilarim, name='yazilarim'),
    path('detay/<slug:slug>', detay, name='detay'),
    path('yaziEkle', yaziEkle, name='yaziEkle'),
    path('yaziGuncelle/<slug:slug>', yaziGuncelle, name='yaziGuncelle'),
    path('yaziSil/<slug:slug>', yaziSil, name='yaziSil'),
    path('yorumSil/<int:id>', yorumSil, name='yorumSil')
]
