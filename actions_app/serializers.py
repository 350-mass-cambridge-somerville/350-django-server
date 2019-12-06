from rest_framework import serializers
from actions_app.models import Action, ActionCard

class ActionSerializer(serializers.Serializer):
    class Meta:
        model = Action
        fields = ['id', 'date', 'description']

class ActionCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionCard
        fields = ['id', 'number', 'date']
