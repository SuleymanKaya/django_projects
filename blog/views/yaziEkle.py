from django.shortcuts import render, redirect
from blog.forms import YaziEkleModelForm
from django.contrib.auth.decorators import login_required

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