from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Host(models.Model):
    cmdbid            = models.CharField(primary_key=True, max_length=15, validators=[RegexValidator('^CMDB[0-9]{11}','invalid CMDB ID')])
    name              = models.CharField(max_length=80) ## by default blank=False, null=False
    product           = models.CharField(max_length=50)
    modified_at       = models.DateTimeField()
    modified_by       = models.CharField(max_length=50)

    def __str__(self):
        return self.cmdbid
     
class HostParameter(models.Model):
    fk                = models.ForeignKey(Host, on_delete=models.CASCADE)
    parameter_section = models.CharField(max_length=40)
    parameter         = models.CharField(max_length=80)
    parameter_index   = models.IntegerField()
    value             = models.CharField(max_length=200, null=True)
    modified_at       = models.DateTimeField()
    modified_by       = models.CharField(max_length=50)

    def __str__(self):
        return self.fk

class Instance(models.Model):
    cmdbid            = models.CharField(primary_key=True, max_length=15, validators=[RegexValidator('^CMDB[0-9]{11}','invalid CMDB ID')])
    name              = models.CharField(max_length=100) ## by default blank=False, null=False
    product           = models.CharField(max_length=25)
    modified_at       = models.DateTimeField()
    modified_by       = models.CharField(max_length=50)
    fk_host           = models.ForeignKey(Host, on_delete=models.CASCADE)

    def __str__(self):
        return self.cmdbid 

class InstanceParameter(models.Model):
    fk                = models.ForeignKey(Instance, on_delete=models.CASCADE)
    parameter_section = models.CharField(max_length=40)
    parameter         = models.CharField(max_length=80)
    parameter_index   = models.IntegerField()
    value             = models.CharField(max_length=200, null=True)
    modified_at       = models.DateTimeField()
    modified_by       = models.CharField(max_length=50)

    def __str__(self):
        return self.fk

class Db(models.Model):
    cmdbid            = models.CharField(primary_key=True, max_length=15, validators=[RegexValidator('^CMDB[0-9]{11}','invalid CMDB ID')])
    name              = models.CharField(max_length=200)
    product           = models.CharField(max_length=25)
    modified_at       = models.DateTimeField()
    modified_by       = models.CharField(max_length=50)
    fk_instance       = models.ForeignKey(Instance, on_delete=models.CASCADE)

    def __str__(self):
        return self.cmdbid 
    #def __str__(self):
    #    return self.name+" @ "+self.fk_instance.name

class DbParameter(models.Model):
    fk                = models.ForeignKey(Db, on_delete=models.CASCADE)
    parameter_section = models.CharField(max_length=40)
    parameter         = models.CharField(max_length=80)
    parameter_index   = models.IntegerField()
    value             = models.CharField(max_length=200, null=True)
    modified_at       = models.DateTimeField()
    modified_by       = models.CharField(max_length=50)

    def __str__(self):
        return self.fk    

class Account(models.Model):
    id                = models.CharField(primary_key=True, max_length=15, validators=[RegexValidator('^AC[0-9]{10}','invalid AC ID')])
    name              = models.CharField(max_length=200)
    modified_at       = models.DateTimeField()
    modified_by       = models.CharField(max_length=50)
    fk_db             = models.ForeignKey(Db, on_delete=models.CASCADE)

    def __str__(self):
        return self.id 

class AccountParameter(models.Model):
    fk                = models.ForeignKey(Account, on_delete=models.CASCADE)
    parameter_section = models.CharField(max_length=40)
    parameter         = models.CharField(max_length=80)
    parameter_index   = models.IntegerField()
    value             = models.CharField(max_length=200, null=True)
    modified_at       = models.DateTimeField()
    modified_by       = models.CharField( max_length=50)

    def __str__(self):
        return self.fk 