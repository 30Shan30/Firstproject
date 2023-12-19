from rest_framework import serializers, status
from rest_framework.response import Response

import requests
import json
from django.conf import settings

from .models import Host,HostParameter,Instance,InstanceParameter,Db,DbParameter,Account,AccountParameter

###Host###
class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = "__all__" 

class HostParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostParameter
        fields = "__all__" 

###Instance###
class InstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instance
        fields = "__all__" 

class InstanceParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstanceParameter
        fields = "__all__" 

###Db###
class DbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Db
        fields = "__all__" 

class DbParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = DbParameter
        fields = "__all__" 

###Account###
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__" 

class AccountParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountParameter
        fields = "__all__" 
