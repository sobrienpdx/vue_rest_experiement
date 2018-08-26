from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User


class Image(models.Model):
	image = models.ImageField(upload_to='images/', blank=True, null=True)
	description = models.CharField(max_length=250, null=True, blank=True)

	def __str__(self):
		if self.description:
			return self.description
		return str(self.image)


class Card(models.Model):
	text = models.TextField()
	images = models.ManyToManyField(Image, related_name="cards", blank=True)
	timestamp = models.DateTimeField(default=datetime.now())

	def __str__(self):
		return self.text


class Set(models.Model):
	title = models.CharField(max_length=250)
	timestamp = models.DateTimeField(default=datetime.now())
	cards = models.ManyToManyField(Card, related_name="sets", blank=True)

	def __str__(self):
		return self.title


class Score(models.Model):
	correct = models.FloatField()
	incorrect = models.FloatField()
	timestamp = models.DateTimeField(default=datetime.now())

	def __str__(self):
		return f'Score: {self.correct / (self.correct + self.incorrect)}'
