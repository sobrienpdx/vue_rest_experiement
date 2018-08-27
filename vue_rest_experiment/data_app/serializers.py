# from django.contrib.auth.models import Card, Set, Score, Image
from rest_framework import serializers
from .models import Card, Set, Score, Image


class ImageSerializer(serializers.HyperlinkedModelSerializer):
	url = serializers.HyperlinkedIdentityField(view_name="data_app:image-detail")
	class Meta:
		model = Image
		fields = ('__all__')


class CardSerializer(serializers.HyperlinkedModelSerializer):
	url = serializers.HyperlinkedIdentityField(view_name="data_app:card-detail")
	images = ImageSerializer(many=True)
	class Meta:
		model = Card
		fields = ('__all__')


class SetSerializer(serializers.HyperlinkedModelSerializer):
	url = serializers.HyperlinkedIdentityField(view_name="data_app:set-detail")
	cards = CardSerializer(many=True)
	class Meta:
		model = Set
		fields = ('__all__')



class ScoreSerializer(serializers.HyperlinkedModelSerializer):
	url = serializers.HyperlinkedIdentityField(view_name="data_app:score-detail")
	class Meta:
		model = Score
		fields = ('__all__')
