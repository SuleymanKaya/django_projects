from django.shortcuts import redirect, get_object_or_404
from blog.models import YorumModel
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='/blog')
def yorumSil(request, id):
    
    yorum = get_object_or_404(YorumModel, id=id)
    if yorum.yazan == request.user or yorum.yazi.yazar == request.user:
        yorum.delete()
        messages.success(request, 'Yorumunuz Başarıyla Silinmiştir')
        return redirect('detay', slug = yorum.yazi.slug)

    return redirect('anasayfa')