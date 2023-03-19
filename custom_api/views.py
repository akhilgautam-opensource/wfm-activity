from django.shortcuts import render
from rest_framework import generics
from .models import WfmActivity
from .serializers import WfmActivitySerializer

class WfmActivityDetail(generics.RetrieveAPIView):
    queryset = WfmActivity.objects.all()
    serializer_class = WfmActivitySerializer