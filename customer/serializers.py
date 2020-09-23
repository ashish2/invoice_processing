from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import *
# from basemodel.views import UserViewSet

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        # fields = ['url', 'username', 'email', 'groups']
        fields = '__all__'
