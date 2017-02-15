from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *

class CustomObtainAuthToken(ObtainAuthToken):

	def post(self, request, *args, **kwargs):
		response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
		token = Token.objects.get(key = response.data['token'])
		user = get_user_model().objects.get(pk = token.user_id)
		return Response({'token': token.key, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email})

class UsersCreate(CreateAPIView):
	model = get_user_model()
	permission_classes = (AllowAny,)
	serializer_class = UserSerializer