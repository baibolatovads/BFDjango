from rest_framework import serializers
from api.models import Task, TaskList
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


class TaskShortSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    task_list_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Task
        fields = ('id', 'name', 'is_done', 'task_list_id',)

    def validate_name(self, value):
        if any(x in value for x in ['%', '&', '$', '^']):
            raise serializers.ValidationError('invalid character in name field')
        return value


class TaskListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    topic = serializers.CharField(required=True)
    tasks_count = serializers.IntegerField(default=0)
    tasks = TaskShortSerializer(many=True, read_only=True)

    class Meta:
        model = TaskList
        fields = ('id', 'topic', 'created_by', 'schedule', 'publisher', 'tasks_count', 'tasks',)

    def validate_name(self, value):
        if any(x in value for x in ['%', '&', '$', '^']):
            raise serializers.ValidationError('invalid character in name field')
        return value


class TaskFullSerializer(TaskShortSerializer):
    task_list = TaskListSerializer(read_only=True)

    class Meta(TaskShortSerializer.Meta):
        fields = TaskShortSerializer.Meta.fields + ('task_list', )












