from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import Group
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.utils.translation import gettext_lazy as _
# Create your serializers here.

User = get_user_model()


class RegisterationSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=60, required=True, validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = ('id', 'username', 'password','email')
        extra_kwargs = {
            'password': {'write_only': True},
        }
        read_only_fields = ('id',)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create_user(
            **validated_data
        )
        user.set_password(password)
        user.save()
        return user



class RefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {
        'bad_token': _('Token is invalid or expired')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')