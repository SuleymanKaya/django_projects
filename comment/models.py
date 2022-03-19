from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from post.models import PostModel

# Create your models here.
class CommentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='post')
    content = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()

        return super(CommentModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.post.title + ' ' + self.user.username

    def children(self):
        return CommentModel.objects.filter(parent=self)
    
    @property
    def any_children(self):
        return CommentModel.objects.filter(parent=self).exists()


