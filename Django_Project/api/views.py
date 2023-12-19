from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view, permission_classes
from django_filters.rest_framework import FilterSet
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.views import APIView

from django.core import serializers
import requests
import json
from django.conf import settings
from .serializers import HostSerializer,HostParameterSerializer,InstanceSerializer,InstanceParameterSerializer, DbSerializer,DbParameterSerializer,AccountSerializer,AccountParameterSerializer
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly, DjangoModelPermissions, IsAdminUser
from django.http import JsonResponse

from .models import *
from Django_Project.scripts.host_request import *

schema_view = get_schema_view(
    openapi.Info(
        title="VIWEB API Interface (" + settings.ENV_SYSTEM + ")",
        default_version="v1",
        description="This page will show you all VI APIS you're allowed to execute!",
        contact=openapi.Contact(email=""),
    )
)



## only sample openapi schema , will be  dynamic json 
@swagger_auto_schema(method='post',
    request_body = openapi.Schema(
        title="Host_HostParameter",
        type=openapi.TYPE_OBJECT,required=['rawdata'],
        properties={
            'rawdata': openapi.Schema(type=openapi.TYPE_ARRAY, description='Host and HostParameter info',
                items=openapi.Schema(type=openapi.TYPE_OBJECT, description='host item',
                    properties={
                        #'type':openapi.Schema(type=openapi.TYPE_STRING, description='type',required='cmdbid'),
                        'cmdbid':openapi.Schema(type=openapi.TYPE_STRING, description='CMDB ID mandatory',required='cmdbid',pattern="^CMDB[0-9]{11}$"),   
                        'name':openapi.Schema(type=openapi.TYPE_STRING, description='Hostname is mandatory',required='name'),    
                        'product':openapi.Schema(type=openapi.TYPE_STRING, description='Product is mandatory',required='product'),
                        'cmdb': openapi.Schema(type=openapi.TYPE_OBJECT,
                                            properties={
                                                'ci_name':openapi.Schema(type=openapi.TYPE_ARRAY,description='ci',items=openapi.Schema(type=openapi.TYPE_STRING, description='ci item')),
                                                    'serialnumber':openapi.Schema(type=openapi.TYPE_ARRAY,description='ci',items=openapi.Schema(type=openapi.TYPE_STRING, description='serialnumber'))
                                                        }
                        )
                    }

                )
            ),
        }
    )
)                           
@api_view(('POST',))
def hostrequest(request):
    data=request.data.get('rawdata')
    print(data)
    result= host_request(data)

    if result:
        my_return = '{"status":"ok"}'
    else:
        my_return = '{"status":"error"}'
    
    return Response(my_return, status=status.HTTP_201_CREATED)

class HostViewFilter(FilterSet):
    """
    Filter for Host
    """

    class Meta:
        model = Host
        fields = '__all__'         
class HostView(viewsets.ModelViewSet):
    """
    GET...  Will list all available Host
    POST... Will create a new Instance parameters entry
    PUT...  Will update a existing Instance parameters entry
    """

    permission_classes = [DjangoModelPermissions]

    queryset = Host.objects.all()
    serializer_class = HostSerializer
    filter_class = HostViewFilter
    http_method_names = ["get","post","put","delete"]  

class HostParameterViewFilter(FilterSet):
    """
    Filter for HostParameter
    """

    class Meta:
        model = HostParameter
        fields = '__all__'         
class HostParameterView(viewsets.ModelViewSet):
    """
    GET...  Will list all available Host
    POST... Will create a new Instance parameters entry
    PUT...  Will update a existing Instance parameters entry
    """

    permission_classes = [DjangoModelPermissions]

    queryset = HostParameter.objects.all()
    serializer_class = HostParameterSerializer
    filter_class = HostParameterViewFilter
    http_method_names = ["get","post","put","delete"] 

#####Instance####
class InstanceViewFilter(FilterSet):
    """
    Filter for Instance
    """

    class Meta:
        model = Instance
        fields = '__all__'   

class InstanceView(viewsets.ModelViewSet):
    """
    GET...  Will list all available Host
    POST... Will create a new Instance parameters entry
    PUT...  Will update a existing Instance parameters entry
    """

    permission_classes = [DjangoModelPermissions]

    queryset = Instance.objects.all()
    serializer_class = InstanceSerializer
    filter_class = InstanceViewFilter
    http_method_names = ["get","post","put","delete"]  

class InstanceParameterViewFilter(FilterSet):
    """
    Filter for InstanceParameter
    """

    class Meta:
        model = InstanceParameter
        fields = '__all__'         
class InstanceParameterView(viewsets.ModelViewSet):
    """
    GET...  Will list all available Host
    POST... Will create a new Instance parameters entry
    PUT...  Will update a existing Instance parameters entry
    """

    permission_classes = [DjangoModelPermissions]

    queryset = InstanceParameter.objects.all()
    serializer_class = InstanceParameterSerializer
    filter_class = InstanceParameterViewFilter
    http_method_names = ["get","post","put","delete"]  

#####Db####
class DbViewFilter(FilterSet):
    """
    Filter for Db
    """

    class Meta:
        model = Db
        fields = '__all__'   

class DbView(viewsets.ModelViewSet):
    """
    GET...  Will list all available Db
    POST... Will create a new Db parameters entry
    PUT...  Will update a existing Db parameters entry
    """

    permission_classes = [DjangoModelPermissions]

    queryset = Db.objects.all()
    serializer_class = DbSerializer
    filter_class = DbViewFilter
    http_method_names = ["get","post","put","delete"]  

class DbParameterViewFilter(FilterSet):
    """
    Filter for DbParameter
    """

    class Meta:
        model = DbParameter
        fields = '__all__'         
class DbParameterView(viewsets.ModelViewSet):
    """
    GET...  Will list all available Db
    POST... Will create a new Db parameters entry
    PUT...  Will update a existing Db parameters entry
    """

    permission_classes = [DjangoModelPermissions]

    queryset = DbParameter.objects.all()
    serializer_class = DbParameterSerializer
    filter_class = DbParameterViewFilter
    http_method_names = ["get","post","put","delete"]  

#####Account####
class AccountViewFilter(FilterSet):
    """
    Filter for Account
    """

    class Meta:
        model = Account
        fields = '__all__'   

class AccountView(viewsets.ModelViewSet):
    """
    GET...  Will list all available Account
    POST... Will create a new Account parameters entry
    PUT...  Will update a existing Account parameters entry
    """

    permission_classes = [DjangoModelPermissions]

    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    filter_class = AccountViewFilter
    http_method_names = ["get","post","put","delete"]  

class AccountParameterViewFilter(FilterSet):
    """
    Filter for AccountParameter
    """

    class Meta:
        model = AccountParameter
        fields = '__all__'         
class AccountParameterView(viewsets.ModelViewSet):
    """
    GET...  Will list all available Account
    POST... Will create a new Account parameters entry
    PUT...  Will update a existing Account parameters entry
    """

    permission_classes = [DjangoModelPermissions]

    queryset = AccountParameter.objects.all()
    serializer_class = AccountParameterSerializer
    filter_class = AccountParameterViewFilter
    http_method_names = ["get","post","put","delete"]  
