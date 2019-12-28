from actions_app.models import Action, ActionCard, SurveyResponse
from actions_app.serializers import ActionCardSerializer, ActionSerializer, SurveyResponseSerializer, SurveyResponsePostSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.models import AnonymousUser
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

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

@api_view(['GET'])
def latest_action_card(request):
    """
    Get the latest action card
    """
    if request.method == 'GET':
        card = ActionCard.objects.latest('date')
        serializer = ActionCardSerializer(card)
        return Response(serializer.data)

    else:
       logger.error('Latest action card got non-get request.')
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SurveyResponseList(generics.ListCreateAPIView):
    queryset = SurveyResponse.objects.all()
    serializer_class = SurveyResponseSerializer

    def perform_create(self, serializer):
        print(self.request.__dict__)
        if isinstance(self.request._user,AnonymousUser):
            print("Not logged in, saving null user")
            serializer.validated_data['user'] = None
        else:
            serializer.validated_data['user'] = self.request.user
        return super(SurveyResponseList, self).perform_create(serializer)

    def get_serializer_class(self):
        """
        Return the class to use for the serializer.
        Defaults to using `self.serializer_class`.

        You may want to override this if you need to provide different
        serializations depending on the incoming request.

        (Eg. admins get full serialization, others get basic serialization)
        """
        assert self.serializer_class is not None, (
            "'%s' should either include a `serializer_class` attribute, "
            "or override the `get_serializer_class()` method."
            % self.__class__.__name__
        )
       
        if self.request.method == 'POST':
            return SurveyResponsePostSerializer
        return self.serializer_class


class SurveyResponseDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = SurveyResponse.objects.all()
    serializer_class = SurveyResponseSerializer