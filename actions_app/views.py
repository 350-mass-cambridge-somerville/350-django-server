from actions_app.models import Action, ActionCard, SurveyResponse, Tag
from actions_app.serializers import ActionCardSerializer, ActionCardPostSerializer, ActionSerializer, SurveyResponseSerializer, SurveyResponsePostSerializer, UserSerializer
from actions_app.permissions import IsOwner
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.contrib.auth.models import AnonymousUser, User
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

@api_view(['GET'])
def current_user(request):
    """
    Get the latest action card
    """
    if request.method == 'GET':
        user = User
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    else:
       logger.error('Current user got non-get request.')
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#class TagList(generics.ListCreateAPIView):
#    permission_classes = [IsAuthenticatedOrReadOnly]
#    queryset = Tag.objects.all()
#    serializer_class = TagSerializer

class ActionList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Action.objects.all()
    serializer_class = ActionSerializer


class ActionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Action.objects.all()
    serializer_class = ActionSerializer

class ActionCardList(generics.ListCreateAPIView):
    queryset = ActionCard.objects.all()
    serializer_class = ActionCardSerializer

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
            return ActionCardPostSerializer
        return self.serializer_class



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
    filterset_fields = ['action_card']

    def perform_create(self, serializer):
        print(self.request.__dict__)
        if isinstance(self.request._user, AnonymousUser):
            print("Not logged in, saving null user")
            serializer.validated_data['user'] = None
        else:
            serializer.validated_data['user'] = self.request.user
            serializer.validated_data['name'] = self.request.user.username
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

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_survey_responses(request):
    """
    Get the survey responses for logged in user
    """
    if request.method == 'GET':
        get_data = request.query_params #or request.GET check both
        print("Query params: "+str(request.query_params))
        responses = SurveyResponse.objects.filter(user=request.user, action_card=get_data['action_card'])
        #print("Queryset is "+str(responses))
        serializer = SurveyResponseSerializer(responses, many=True)
        return Response(serializer.data)

    else:
       logger.error('User survey responses got non-get request.')
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SurveyResponseDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = SurveyResponse.objects.all()
    serializer_class = SurveyResponseSerializer
