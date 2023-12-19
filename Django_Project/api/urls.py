from django.urls import include, path, re_path
from django.views.generic.base import RedirectView
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here

from . import views


router = routers.SimpleRouter()
#router.register(r"vmguard", views.GuardianofthevgalaxyView)
router.register(r"Host", views.HostView)
router.register(r"HostParameter", views.HostParameterView)
router.register(r"Instance", views.InstanceView)
router.register(r"InstanceParameter", views.InstanceParameterView)
router.register(r"Db", views.DbView)
router.register(r"DbParameter", views.DbParameterView)
router.register(r"Account", views.AccountView)
router.register(r"AccountParameter", views.AccountParameterView)

urlpatterns = [
    re_path(r'^(?P<version>v1)/swagger(?P<format>\.json|\.yaml)$',
        views.schema_view.without_ui(cache_timeout=0), 
        name='schema-json'),
    re_path(r'^(?P<version>v1)/swagger/$', 
        views.schema_view.with_ui('swagger', cache_timeout=0), 
        name='schema-swagger-ui'),
    re_path(r'^v1/redoc/$', 
        views.schema_view.with_ui('redoc', cache_timeout=0), 
        name='schema-redoc'),
    re_path(r"(?P<version>v1)/", include(router.urls), name="v1"),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r"(?P<version>v1)/generateApiToken/", obtain_auth_token, name='api_token_auth'),
   # re_path(r"v1/insertcmdbhost/",views.insertcmdbhost),
   # re_path(r"v1/put/",views.put),
    re_path(r"v1/hostrequest/",views.hostrequest)
    #re_path(r"v1/host/", views.host_list)
]