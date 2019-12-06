from actions_app.models import Action, ActionCard
from actions_app.serializers import ActionCardSerializer, ActionSerializer
from rest_framework import generics


class ActionList(generics.ListCreateAPIView):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer


class ActionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer

class ActionCardList(generics.ListCreateAPIView):
    queryset = ActionCard.objects.all()
    serializer_class = ActionCardSerializer


class ActionCardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ActionCard.objects.all()
    serializer_class = ActionCardSerializer