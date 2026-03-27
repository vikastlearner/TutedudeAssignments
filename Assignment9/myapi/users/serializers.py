from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source="created_by.username", read_only=True)
    class Meta:
        model = User
        fields = ('__all__')
        read_only_fields = ('created_by',) #created by is only for reading and no write and this shall be tupple/list

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return User.objects.create(**validated_data)

