from django.db import models
from django.utils import simplejson
# Create your models here.
class Scripture(models.Model):
	title = models.CharField(max_length=50)
	text = models.CharField(max_length=2000)
	comment = models.CharField(max_length=2000)
	badge_url = models.CharField(max_length=2000)
	reference = models.CharField(max_length=50)
	view_date = models.DateTimeField()

	def serializeForJson(self):
		to_json = {
			"title": self.title,
			"text": self.text,
			"comment": self.comment,
			"badge_url": self.badge_url,
			"reference": self.reference,
    	}
		return to_json

	def __unicode__(self):
		return self.title

class Question(models.Model):
	scripture = models.ForeignKey(Scripture)
	question_text = models.CharField(max_length = 200)
	position = models.IntegerField(default=0)
	def serializeForJson(self):
		to_json = {
			"position": self.position,
			"question_text": self.question_text,
    	}
		return to_json
	def __unicode__(self):
		return self.question_text

class Trait(models.Model):
	scripture = models.ForeignKey(Scripture)

	HOPE = 'HOPE'
	FAITH = 'FAITH'
	LOVE = 'LOVE'
	LIGHT = 'LIGHT'

	TRAIT_CHOICES = (
		(HOPE, 'Hope'),
		(FAITH, 'Faith'),
		(LOVE, 'Love'),
		(LIGHT, 'Light'),
		)
	trait = models.CharField(max_length = 10, choices = TRAIT_CHOICES)
	def serializeForJson(self):
		to_json = {
			"trait": self.trait,
    	}
		return to_json
	def __unicode__(self):
		return self.trait