from django.db import models

# Create your models here.
class Action(models.Model):
	date = models.DateField(auto_now_add=True)
	start_date = models.DateField(auto_now_add=True)
	end_date = models.DateField(auto_now_add=True)
	description = models.CharField(max_length=50000)

class ActionCard(models.Model):
	date = models.DateField(auto_now_add=True)
	number = models.IntegerField()

class SurveyResponse(models.Model):
	date = models.DateField(auto_now_add=True)