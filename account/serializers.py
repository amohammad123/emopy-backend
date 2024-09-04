from rest_framework import serializers
from .models import *


class UserDetailSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        res = super().to_representation(instance)
        res['image'] = instance.image if hasattr(instance, 'image') and instance.image else None
        return res

    class Meta:
        fields = ['id', 'username', 'first_name', 'last_name', 'is_therapist']
        model = User
