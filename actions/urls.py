"""actions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from actions_app import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    re_path(r'^rest-auth/', include('rest_auth.urls')),
    re_path(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    path('admin/', admin.site.urls),
    path('actions/', views.ActionList.as_view()),
    path('actions/<int:pk>/', views.ActionDetail.as_view()),
    path('actioncards/', views.ActionCardList.as_view()),
    path('actioncards/latest/', views.latest_action_card),
    path('actioncards/<int:pk>/', views.ActionCardDetail.as_view()),
    path('surveyresponses/', views.SurveyResponseList.as_view()),
    path('surveyresponses/<int:pk>/', views.SurveyResponseDetail.as_view()),
    #path('tags/', views.TagList.as_view()),
    path('user/', views.current_user),
    path('surveyresponses/user/', views.user_survey_responses),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
