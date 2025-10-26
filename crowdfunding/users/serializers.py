from rest_framework import serializers
from .models import CustomUser
 
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': { 'write_only': True } }

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
        # The ** is related to kwargs

    def update(self, instance, validated_data):
        # Remove password from validated_data if present, handle it separately
        password = validated_data.pop('password', None)

        # Update all other fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        # Handle password separately if provided - however this is not supported
        # if password:
        #     instance.set_password(password)

        instance.save()
        return instance
