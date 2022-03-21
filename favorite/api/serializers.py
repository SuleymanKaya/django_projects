from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from favorite.models import FavoriteModel

class FavoriteListCreateAPISerializer(ModelSerializer):
    class Meta:
        model = FavoriteModel
        fields = '__all__'

    def validate(self, attrs):
        queryset = FavoriteModel.objects.filter(user=attrs['user'], post=attrs['post'])
        if queryset.exists():
            raise serializers.ValidationError("Bu post zaten favorilere eklendi")
        return attrs

class FavoriteAPISerializer(ModelSerializer):
    class Meta:
        model = FavoriteModel
        fields = ('content',)