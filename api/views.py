from django.shortcuts import render
from django.http import JsonResponse


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerialiazer
from .models import Task
import emoji
# Create your views here.
@api_view(['GET'])
def apiView(request):
    api_urls = {
        'lists': '/task-list/',
        'Detail-view':'/task-detail/<str:pk>/',
        'create':'/task-create/',
        'update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def tasklist(request):
    task = Task.objects.all()
    serializer = TaskSerialiazer(task,many=True)
    return Response(serializer.data)
@api_view(['GET'])
def taskdetail(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerialiazer(task,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskcreate(request):
   serializer = TaskSerialiazer(data = request.data)
   
   if serializer.is_valid():
       serializer.save()
       return Response(serializer.data)
   
@api_view(['POST'])
def taskUpdate(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerialiazer(instance = task, data = request.data)
    if serializer.is_valid():
       serializer.save()
       return Response(serializer.data)
   
   
      
@api_view(['DELETE'])
def taskDelete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response(emoji.emojize("successfully deleted your activity :thumps_up:!"))