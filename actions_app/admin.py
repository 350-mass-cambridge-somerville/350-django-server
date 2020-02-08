from django.contrib import admin
from actions_app.models import Action, ActionCard, SurveyResponse
# Register your models here.
admin.site.register(Action)
admin.site.register(ActionCard)
admin.site.register(SurveyResponse)