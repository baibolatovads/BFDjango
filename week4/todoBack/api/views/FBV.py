from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from api.models import Task
from api.serializers import TaskSerializer

@api_view(['GET', 'POST'])
def task_list(request):
    if request == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
def task_list_detail(request, pk):
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist as e:
        return Response({'error': '{e}'}, status=status.HTTP_404_NOT_FOUND)
    if request == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request == 'PUT':
        serializer = TaskSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    if request == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response({'error': 'bad request'})