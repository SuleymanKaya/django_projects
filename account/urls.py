from django.urls import path
from account.views import cikis, sifreDegistirme, profilGuncelle, kayit, ProfilDetailView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cikis', cikis, name='cikis'),
    path('sifreDegistirme', sifreDegistirme, name='sifreDegistirme'),
    path('profilGuncelle', profilGuncelle, name='profilGuncelle'),
    path('kayit', kayit, name='kayit'),
    path('giris', auth_views.LoginView.as_view(template_name = 'pages/giris.html'), name='giris'),
    path('profil/<str:username>', ProfilDetailView.as_view(), name='profil')
]