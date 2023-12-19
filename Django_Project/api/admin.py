from django.contrib import admin
from .models import Host,HostParameter,Instance,InstanceParameter,Db,DbParameter,Account,AccountParameter

glb_filter = ['parameter', 'parameter_section' ]

# Register your models here.

@admin.register(Host)
class HostAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Host._meta.fields]
    search_fields = ['cmdbid','product']
    list_filter = ['product']

@admin.register(HostParameter)
class HostParameterAdmin(admin.ModelAdmin):
    list_display = [field.name for field in HostParameter._meta.fields]
    search_fields = ['parameter_section','parameter']
    list_filter = search_fields
@admin.register(Instance)
class InstanceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Instance._meta.fields]
    search_fields = ['cmdbid','product']
    list_filter = ['product']

@admin.register(InstanceParameter)
class InstanceParameterAdmin(admin.ModelAdmin):
    list_display = [field.name for field in InstanceParameter._meta.fields]
    search_fields = ['parameter_section','parameter']
    list_filter = search_fields
@admin.register(Db)
class DbAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Db._meta.fields]
    search_fields = ['cmdbid','product']
    list_filter = ['product']

@admin.register(DbParameter)
class DbParameterAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DbParameter._meta.fields]
    search_fields = ['parameter_section','parameter']
    list_filter = search_fields
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Account._meta.fields]
    search_fields = ['id']
    list_filter = ['id']

@admin.register(AccountParameter)
class AccountParameterAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AccountParameter._meta.fields]
    search_fields = ['parameter_section','parameter']
    list_filter = search_fields