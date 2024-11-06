from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import generics
from api.models import MyModel
from api.serializers import MyModelSerializer


class MyModelListCreate(generics.ListCreateAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer


class MyModelRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer


def index(request):
    return HttpResponse("api")
