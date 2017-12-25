from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    confirmPassword = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirmPassword')

    def validate(self, data):

        if data['password'] != data['confirmPassword']:
            raise serializers.ValidationError({"confirmPassword": "Passwords do not match"})
        return data


class UserBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'email', 'first_name', 'last_name')


class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name', required=False)
    last_name = serializers.CharField(source='user.last_name', required=False)
    email = serializers.CharField(source='user.email')
    user_id = serializers.PrimaryKeyRelatedField(source='user.id', read_only=True)

    class Meta:
        model = UserProfile
        fields = ('user_id', 'email', 'profile_image', 'bio', 'username', 'first_name', 'last_name')
        extra_kwargs = {'bio': {'required': False}, 'profile_image': {'required': False}}

    def update(self, instance, validated_data):
        user_dict = validated_data.get('user')
        user = instance.user
        user.email = user_dict.get('email', user.email)
        user.first_name = user_dict.get('first_name', user.first_name)
        user.last_name = user_dict.get('last_name', user.last_name)
        user.save()
        instance.bio = validated_data.get('bio', None)
        instance.profile_image = validated_data.get('profile_image', None)
        instance.save()
        return instance


