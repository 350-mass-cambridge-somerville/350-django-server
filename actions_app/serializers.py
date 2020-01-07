from rest_framework import serializers
from actions_app.models import Action, ActionCard, SurveyResponse
from django.contrib.auth.models import User
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_superuser']
#class TagSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Tag
#        fields = "__all__" #['id', 'number', 'date', 'actions', 'survey_responses']


class SurveyResponseSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    name = serializers.HiddenField(default='Anonymous')
    class Meta:
        model = SurveyResponse
        fields = ['id', 'date', 'name', 'user', 'action_card', 'actions']

class SurveyResponsePostSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    #name = serializers.HiddenField(default='Anonymous')
    class Meta:
        model = SurveyResponse
        fields = ['id', 'date', 'name', 'user', 'action_card', 'actions']

class ActionSerializer(serializers.ModelSerializer):
    #tags = TagSerializer(many=True, read_only=True)
    taggit = TagListSerializerField()
    
    class Meta:
        model = Action
        fields = ['id', 'date', 'description', 'date_type', 'taggit', 'geography_type', 'start_date', 'end_date']
    
    def create(self, validated_data):
        tags = validated_data.pop('taggit')
        instance = super(ActionSerializer, self).create(validated_data)
        instance.taggit.set(*tags)
        return instance
class ActionCardSerializer(serializers.ModelSerializer):
    survey_responses = SurveyResponseSerializer(many=True, read_only=True)
    actions = ActionSerializer(many=True, read_only=True)
    class Meta:
        model = ActionCard
        fields = "__all__" #['id', 'number', 'date', 'actions', 'survey_responses']

class ActionCardPostSerializer(serializers.ModelSerializer):
    #actions = ActionSerializer(many=True, read_only=True)
    class Meta:
        model = ActionCard
        fields = "__all__" #['id', 'number', 'date', 'actions', 'survey_responses']
