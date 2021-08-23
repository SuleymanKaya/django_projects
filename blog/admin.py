from django.contrib import admin
from blog.models import KategoriModel, YazilarModel, YorumModel


# Register your models here.
admin.site.register(KategoriModel)

class YazilarAdmin(admin.ModelAdmin):
    search_fields = ('baslik', 'icerik')
    list_display = ('baslik', 'olusturma_tarihi', 'duzenleme_tarihi')

admin.site.register(YazilarModel, YazilarAdmin)

class YorumAdmin(admin.ModelAdmin):
    list_display = ('yazan', 'olusturma_tarihi', 'guncelleme_tarihi')
    search_fields = ('yazan__username',)

admin.site.register(YorumModel, YorumAdmin)
