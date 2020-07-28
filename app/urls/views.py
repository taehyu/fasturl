# from django.db.migrations import serializer
# from django.shortcuts import render
#
# # Create your views here.
# from rest_framework import status
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from rest_framework.viewsets import ModelViewSet
#
# from urls.models import Url
# from urls.serializers import UrlSerializer
#
#
# class UrlViewSet(ModelViewSet):
#     queryset = Url.objects.all()
#     serializer_class = UrlSerializer
#
#     @action(methods=['Post'], detail=False)
#     def shorten(self, request):
#         print(request.data)
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response(data=serializer.data, status=status.HTTP_201_CREATED)

from django.shortcuts import redirect
from rest_framework import viewsets

from .models import Link
from .serializers import LinkSerializer


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(owner=self.request.user)
        else:
            serializer.save()
