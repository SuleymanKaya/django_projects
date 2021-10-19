from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.forms import ProfilGuncelleForm

@login_required(login_url='/blog')
def profilGuncelle(request):
    if request.method == 'POST':
        form = ProfilGuncelleForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profiliniz Başarıyla Güncellenmiştir')
    else:
        form = ProfilGuncelleForm(instance=request.user)
    return render(request, 'pages/profilGuncelleme.html', context={
        'form':form
    })