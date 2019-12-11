from django.db import models

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
	date = models.DateField(auto_now_add=True)
	name = models.CharField(max_length=500)
	actions = models.ManyToManyField(Action)
	action_card = models.ForeignKey(ActionCard, on_delete=models.PROTECT, related_name='survey_responses')