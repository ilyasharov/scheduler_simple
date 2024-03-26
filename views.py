from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


@login_required
def index(request):
    return render(request, 'index.html')


class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get('name', None)
        description = self.request.query_params.get('description', None)
        status = self.request.query_params.get('status', None)

        if name:
            queryset = queryset.filter(Q(name__icontains=name))
        if description:
            queryset = queryset.filter(Q(description__icontains=description))
        if status:
            queryset = queryset.filter(status=status)
        return queryset


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)


@api_view(['POST'])
@login_required
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
