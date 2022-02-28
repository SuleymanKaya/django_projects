from rest_framework import serializers
from post.models import PostModel

# ModelSerializer kullanımı
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ['title', 'content', 'created', 'slug', 'image']

# Serializer kullanımı
#class PostSerializer(serializers.Serializer):
    #title = serializers.CharField(max_length=150)
    #content = serializers.CharField(max_length=150)