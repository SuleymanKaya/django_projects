from rest_framework import serializers
from post.models import PostModel

# ModelSerializer kullanımı
class PostSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='post:detail',
        lookup_field='slug'
    )
    username = serializers.SerializerMethodField()
    class Meta:
        model = PostModel
        fields = ['username','title', 'content', 'created', 'url', 'image', 'modified_by']

    def get_username(self, obj):
        return str(obj.user.username)

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