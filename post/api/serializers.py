from rest_framework import serializers
from post.models import PostModel

# ModelSerializer kullanımı
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ['user','title', 'content', 'created', 'slug', 'image', 'modified_by']

class PostUpdateCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ['title', 'content', 'image']

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        #instance.content = "Hep aynı content"
        instance.save()
        return instance

    def validate(self, attrs):
        if attrs["title"]=="süleyman":
            raise serializers.ValidationError("Bu değer girilemez")
        return attrs

# Serializer kullanımı
#class PostSerializer(serializers.Serializer):
    #title = serializers.CharField(max_length=150)
    #content = serializers.CharField(max_length=150)