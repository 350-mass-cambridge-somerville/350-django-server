from actions_app.models import Action, ActionCard, SurveyResponse
from actions_app.serializers import ActionCardSerializer, ActionSerializer, SurveyResponseSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ActionList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Action.objects.all()
    serializer_class = ActionSerializer


class ActionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Action.objects.all()
    serializer_class = ActionSerializer

class ActionCardList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ActionCard.objects.all()
    serializer_class = ActionCardSerializer


class ActionCardDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ActionCard.objects.all()
    serializer_class = ActionCardSerializer

class SurveyResponseList(generics.ListCreateAPIView):
    queryset = SurveyResponse.objects.all()
    serializer_class = SurveyResponseSerializer


class SurveyResponseDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = SurveyResponse.objects.all()
    serializer_class = SurveyResponseSerializer