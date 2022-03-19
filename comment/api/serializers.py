from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from comment.models import CommentModel


class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = CommentModel
        exclude = ['created',]


    def validate(self, attrs):
        if (attrs['parent']):
            if attrs['parent'].post != attrs['post']:
                raise serializers.ValidationError("Bir şeyler yanlış gitti.")
        return attrs

class CommentListSerializer(ModelSerializer):
    replies = SerializerMethodField()
    class Meta:
        model = CommentModel
        fields = '__all__'

    def get_replies(self, obj):
        if obj.any_children:
            return CommentListSerializer(obj.children(), many=True).data

class CommentDeleteUpdateSerializer(ModelSerializer):
    class Meta:
        model = CommentModel
        fields = ['content',]
