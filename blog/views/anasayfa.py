from django.shortcuts import render

def anasayfa(request):
    
    cnt = {
        'isim':'Süleyman Kaya-Yazılım Mühendisi',
    }

    return render(request, 'pages/anasayfa.html', context=cnt)