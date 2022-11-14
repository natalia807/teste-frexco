from rest_framework import serializers, status
from rest_framework.exceptions import NotFound
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from django.db import IntegrityError
from frexco.apps.users.exceptions import UserAlreadyExists

from .models import User
from .renderers import UserJSONRenderer
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework_xml.renderers import XMLRenderer
from drf_excel.renderers import XLSXRenderer

from .serializers import UserSerializer


class UserRetrieveAPIView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    renderer_classes = (BrowsableAPIRenderer,JSONRenderer, XMLRenderer, XLSXRenderer )
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
      
        serializer = self.serializer_class(instance=self.get_queryset(),  many=True, context={
            'request': request
        })

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserControllerAPI(APIView):
    #permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserSerializer

    def post(self, request):        

        user = dict(request.POST.items())

        try:
            userObj = User(
                login=user.get('login'),
                password= user.get('password'),
                dateNasc= user.get('dateNasc')
            )
            userObj.save()
        except IntegrityError :
            raise UserAlreadyExists('A User with this username already exists.')
    
        userObjResult = self.serializer_class(userObj, context={
            'request': request
        })

        return Response(userObjResult.data, status=status.HTTP_201_CREATED)