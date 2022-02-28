from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

class PostModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=150)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()
    slug = models.SlugField(unique=True, max_length=150, editable=False)
    image = models.ImageField(upload_to = "media/post/", blank=True)
    
    def get_slug(self):
        slug = slugify(self.title.replace("ı", "i"))
        unique = slug
        number = 1

        while PostModel.objects.filter(slug = unique).exists():
            unique = "{}-{}".format(slug, number)
            number += 1
        
        return unique

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()

        self.slug = self.get_slug()

        return super(PostModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


