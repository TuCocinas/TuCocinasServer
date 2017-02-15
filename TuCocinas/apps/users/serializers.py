from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only = True)

	class Meta:
		model = get_user_model()
		fields = ('username', 'email', 'first_name', 'last_name', 'password')

	def create(self, validated_data):
		user = get_user_model().objects.create(
			username = validated_data['email'],
			email = validated_data['email'],
			first_name = validated_data['first_name'],
			last_name = validated_data['last_name']
		)
		user.set_password(validated_data['password'])
		user.save()
		user_token = Token.objects.create(user = user)
		user_token.save()
		return user