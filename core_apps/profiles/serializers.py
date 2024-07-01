from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    username = serializers.CharField(source="user.username")
    full_name = serializers.CharField(source="user.get_full_name")
    avatar = serializers.SerializerMethodField()
    date_joined = serializers.DateTimeField(source="user.date_joined", read_only=True)

    class Meta:
        model = Profile
        fields = [
            "id", "slug", "first_name", "last_name", "username", "full_name",
            "gender", "bio", "occupation", "date_joined", "avatar",
        ]

    def get_avatar(self, obj:Profile)-> str | None:
        try:
            return obj.avatar.url
        except AttributeError:
            return None
    

class UpdateProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    username = serializers.CharField(source="user.username")

    class Meta:
        model = Profile
        fields = [
            "first_name", "last_name", "username",
            "gender", "bio", "occupation", "avatar", "phone_number",
        ]

class AvatarUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["avatar"]