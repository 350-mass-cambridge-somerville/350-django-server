from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Action(models.Model):
	date = models.DateField(auto_now_add=True)
	start_date = models.DateField(auto_now_add=True)
	end_date = models.DateField(auto_now_add=True)
	description = models.TextField()

class ActionCard(models.Model):
	date = models.DateField(auto_now_add=True)
	number = models.IntegerField()
	actions = models.ManyToManyField(Action)

class SurveyResponse(models.Model):
	user = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, related_name='survey_responses')
	date = models.DateField(auto_now_add=True)
	name = models.CharField(max_length=500)
	actions = models.ManyToManyField(Action)
	action_card = models.ForeignKey(ActionCard, on_delete=models.PROTECT, related_name='survey_responses')