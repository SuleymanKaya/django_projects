#from django.shortcuts import redirect, get_object_or_404
#from django.contrib.auth.decorators import login_required
from blog.models import YazilarModel
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class YaziSilDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('giris')
    template_name = 'pages/yaziSilOnay.html'
    context_object_name = 'yazi_object'
    success_url = reverse_lazy('yazilarim')

    def get_queryset(self):
        yazi = YazilarModel.objects.filter(slug=self.kwargs['slug'], yazar=self.request.user)
        return yazi
"""
@login_required(login_url='/blog')
def yaziSil(request, slug):
    
    get_object_or_404(YazilarModel, slug=slug, yazar=request.user).delete()
    return redirect('yazilarim')
"""   