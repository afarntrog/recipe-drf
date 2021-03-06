from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _ # This puts text throuhg language file so i can later add transalations
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'name') # Will be serialized to json
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}} # Make sure password is valid
    
    # Override stuff
    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data) # Unzip validated data and createuser.



class AuthTokenSerializer(serializers.Serializer):
    """ Serializer user auth object"""
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )


    # attrs is composed of fields that are in our serializers
    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        if not user:
            msg == _('Unable to authenticate with credentials')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user

        return attrs