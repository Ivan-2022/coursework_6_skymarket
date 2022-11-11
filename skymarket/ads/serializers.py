from phonenumber_field import serializerfields
from rest_framework import serializers

from .models import Comment, Ad


class CommentSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField(source="author.id", read_only=True)
    ad_id = serializers.IntegerField(source="ad.id", read_only=True)
    author_first_name = serializers.CharField(source="author.first_name", read_only=True)
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)
    author_image = serializers.ImageField(source="author.image", read_only=True)

    class Meta:
        model = Comment
        fields = ["pk", "text", "created_at", "author_id", "ad_id", "author_first_name", "author_last_name",
                  "author_image"]


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = [
            "pk", "title", "price", "description", "created_at", "image"
        ]


class AdDetailSerializer(serializers.ModelSerializer):
    author_first_name = serializers.ReadOnlyField(source="author.first_name")
    author_last_name = serializers.ReadOnlyField(source="author.last_name")
    phone = serializerfields.PhoneNumberField(source="author.phone", read_only=True)
    author_id = serializers.ReadOnlyField(source="author.id")

    class Meta:
        model = Ad
        fields = [
            "pk", "title", "price", "description", "image", "author_first_name", "author_last_name", "phone",
            "author_id"
        ]
