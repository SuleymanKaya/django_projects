from django.shortcuts import render

def iletisim(request):
    
    cnt = {
        'key': "büyük başlık yapma konusu",
    }

    return render(request, 'pages/iletisim.html', context=cnt)