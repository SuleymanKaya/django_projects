from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from comment.models import CommentModel
from django.contrib.auth.models import User

from post.models import PostModel 


class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = CommentModel
        exclude = ['created',]


    def validate(self, attrs):
        if (attrs['parent']):
            if attrs['parent'].post != attrs['post']:
                raise serializers.ValidationError("Bir şeyler yanlış gitti.")
        return attrs

class CommentUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('is_superuser',)
        #exclude = ('password',)

class CommentPostSerializer(ModelSerializer):
    class Meta:
        model = PostModel
        exclude = ('content', 'draft', 'created', 'modified', 'slug', )

class CommentListSerializer(ModelSerializer):
    replies = SerializerMethodField()
    user = CommentUserSerializer()
    post = CommentPostSerializer()
    class Meta:
        model = CommentModel
        fields = '__all__'
        #depth = 1

    def get_replies(self, obj):
        if obj.any_children:
            return CommentListSerializer(obj.children(), many=True).data

class CommentDeleteUpdateSerializer(ModelSerializer):
    class Meta:
        model = CommentModel
        fields = ['content',]
