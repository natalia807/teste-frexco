
  
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import  UserControllerAPI, UserRetrieveAPIView

urlpatterns = []

urlpatterns.append(path('user/list', UserRetrieveAPIView.as_view()))
urlpatterns.append(path('user/new', UserControllerAPI.as_view()))