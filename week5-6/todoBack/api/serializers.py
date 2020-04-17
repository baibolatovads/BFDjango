from rest_framework import serializers
from models import Task, TaskList
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


class TaskModelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    class Meta:
        model = Task
        fields = ('id', 'name', 'is_done',)

    def validate_name(self, value):
        if any(x in value for x in ['%', '&', '$', '^']):
            raise serializers.ValidationError('invalid character in name field')
        return value


class TaskListShortSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    topic = serializers.CharField(required=True)
    task_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = TaskList
        fields = ('id', 'topic', 'task_id', 'created_by')

    def validate_name(self, value):
        if any(x in value for x in ['%', '&', '$', '^']):
            raise serializers.ValidationError('invalid character in name field')
        return value


class TaskListFullSerializer(TaskListShortSerializer):
    task = TaskModelSerializer(read_only=True)

    class Meta(TaskListShortSerializer.Meta):
        fields = TaskListShortSerializer.Meta.fields + ('task', )





