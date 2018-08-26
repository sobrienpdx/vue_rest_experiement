# from django.contrib.auth.models import Card, Set, Score, Image
from rest_framework import serializers
from .models import Card, Set, Score, Image


class CardSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Card
		fields = ('__all__')


class SetSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Set
		fields = ('__all__')


class ImageSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Image
		fields = ('__all__')


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Score
		fields = ('__all__')
