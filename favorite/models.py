from django.db import models
from django.contrib.auth.models import User
from post.models import PostModel

# Create your models here.
class FavoriteModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return str(self.user) + ' ' + str(self.post)

