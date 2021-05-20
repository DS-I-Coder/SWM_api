from django.shortcuts import render
from rest_framework import serializers, viewsets
from theapp.models import userInfo
from theapp.serializers import userInfoSerializer

# Create your views here.
class userInfoViewSet(viewsets.ModelViewSet):
    queryset = userInfo.objects.all()
    serializer_class = userInfoSerializer

