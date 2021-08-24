from django.db import models

class IletisimModel(models.Model):
    email = models.EmailField(max_length=200)
    isim_soyad = models.CharField(max_length=100)
    mesaj = models.TextField()
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'iletisim'
        verbose_name = 'iletisim'
        verbose_name_plural = 'iletisim'

    def __str__(self):
        return self.email