from django.shortcuts import render

def iletisim(request):
    
    cnt = {
        'isim':'Süleyman Kaya-İletisim Bilgileri',
    }

    return render(request, 'pages/iletisim.html', context=cnt)