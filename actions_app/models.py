from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
GEOGRAPHY_TYPE_CHOICES = [
	['LOCAL', 'Local'],
	['REGIONAL', 'Regional'],
	['STATE', 'State'],
	['NATIONAL', 'National'],
	['UNDEFINED', 'Undefined']
]

class GeographyTypeEnum(object):
	LOCAL = 'LOCAL'
	REGIONAL = 'REGIONAL'
	STATE = 'STATE'
	NATIONAL = 'NATIONAL'
	UNDEFINED = 'UNDEFINED'

DATE_TYPE_CHOICES = [
	['ON', 'on'],
	['BEFORE', 'before'],
	['RANGE', 'range'],
	['NONE', 'none']
]

class DateTypeEnum(object):
	ON = 'ON'
	BEFORE = 'BEFORE'
	RANGE = 'RANGE'
	NONE = 'NONE'

class Tag(models.Model):
	tag = models.CharField(max_length=500)

class Action(models.Model):
	date = models.DateField(default=datetime.date.today)
	start_date = models.DateField(default=datetime.date.today)
	end_date = models.DateField(default=datetime.date.today)
	tags = models.ManyToManyField(Tag, blank=True)
	geography_type = models.CharField(choices=GEOGRAPHY_TYPE_CHOICES, 
                default=GeographyTypeEnum.UNDEFINED, 
                max_length=100)
	date_type = models.CharField(choices=DATE_TYPE_CHOICES, 
			default=DateTypeEnum.NONE, 
			max_length=100)
	description = models.TextField()

class ActionCard(models.Model):
	date = models.DateField(default=datetime.date.today)
	number = models.IntegerField()
	actions = models.ManyToManyField(Action)

class SurveyResponse(models.Model):
	user = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, related_name='survey_responses')
	date = models.DateField(auto_now_add=True)
	name = models.CharField(max_length=500)
	actions = models.ManyToManyField(Action)
	action_card = models.ForeignKey(ActionCard, on_delete=models.PROTECT, related_name='survey_responses')