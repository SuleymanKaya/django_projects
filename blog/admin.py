from django.contrib import admin
from blog.models import KategoriModel, YazilarModel


# Register your models here.
admin.site.register(KategoriModel)

class YazilarAdmin(admin.ModelAdmin):
    search_fields = ('baslik', 'icerik')
    list_display = ('baslik', 'olusturma_tarihi', 'duzenleme_tarihi')

admin.site.register(YazilarModel, YazilarAdmin)
