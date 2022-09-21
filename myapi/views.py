from django.shortcuts import render, redirect
from rest_framework import generics, viewsets
from .serializers import ItemSerializer
from .models import Item


def home(request):
    return render(request, 'myapi/index.html')

class ItemViewSet(viewsets.ModelViewSet):
        queryset = Item.objects.all()
        serializer_class = ItemSerializer

# class ItemAPIView(generics.RetrieveAPIView):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer
#
#
# class ItemAPIList(generics.ListCreateAPIView):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer
#
#
# class ItemAPIUpdate(generics.RetrieveUpdateAPIView):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer
#
#
# class ItemAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer

