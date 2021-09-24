from enum import unique
from django.db import models
from autoslug import AutoSlugField
from blog.models import KategoriModel
from account.models import CustomUserModel
from ckeditor.fields import RichTextField
from blog.abstract_models import DateAbstractModel

class YazilarModel(DateAbstractModel):
    resim = models.ImageField(upload_to="yazi_resimleri")
    baslik = models.CharField(max_length=50)
    icerik = RichTextField()
    slug = AutoSlugField(populate_from="baslik", unique=True)
    kategoriler = models.ManyToManyField(KategoriModel, related_name="yazi")
    yazar = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name="yazilar")

    class Meta:
        verbose_name = "Yazi"
        verbose_name_plural = "Yazilar"
        db_table = "yazi"

    def __str__(self):
        return self.baslik

