from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

@login_required(login_url='/blog')
def sifreDegistirme(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            kullanici = form.save()
            update_session_auth_hash(request, kullanici)
            messages.success(request, 'Şifreniz Başarıyla Değiştirilmiştir')
            return redirect('sifreDegistirme')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'pages/sifreDegistirme.html', context={
        'form':form
    })