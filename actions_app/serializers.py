from rest_framework import serializers
from actions_app.models import Action, ActionCard, SurveyResponse


class SurveyResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyResponse
        fields = ['id', 'name', 'date', 'action_card', 'actions']

class ActionCardSerializer(serializers.ModelSerializer):
    survey_responses = SurveyResponseSerializer(many=True, read_only=True)
    #actions = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = ActionCard
        fields = "__all__" #['id', 'number', 'date', 'actions', 'survey_responses']

class ActionSerializer(serializers.ModelSerializer):
    action_cards = ActionCardSerializer(many=True, read_only=True)
    
    class Meta:
        model = Action
        fields = ['id', 'date', 'description', 'action_cards']
