from django.shortcuts import render
from django.http import HttpResponse
# from django.contrib.auth.models import Image, Card, Set, Score
from rest_framework import viewsets
from .serializers import ImageSerializer, SetSerializer, ScoreSerializer, CardSerializer
from .models import Card, Set, Score, Image


class ImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Image instances to be viewed or edited.
    """
    queryset = Image.objects.all().order_by('-date_joined')
    serializer_class = ImageSerializer


class SetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Set to be viewed or edited.
    """
    queryset = Set.objects.all()
    serializer_class = SetSerializer

class CardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Card to be viewed or edited.
    """
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class ScoreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Score to be viewed or edited.
    """
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
