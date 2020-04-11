from rest_framework import serializers
from models import Task
from auth_.models import MyUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'username', 'email')


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    def create(self, validated_data):
        new_task = Task(**validated_data)
        new_task.save()
        return new_task

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.is_done = validated_data.get('is_done', instance.is_done)
        instance.save()
        return instance


