from __future__ import unicode_literals

from django.db import models


class Privilege(models.Model):
    namePrivilege = models.CharField(db_column=u'Nombre del Privilegio', primary_key=True, max_length=128)
    isBlock = models.BooleanField(db_column=u'Bloqueado', blank=True)
    appliedRules = models.ManyToManyField(Rule, db_column=u'Reglas aplicadas')
        
    class Meta:
        managed = False
        db_table = 'Privilegios'
        
class Surfer(models.Model):
    username = models.CharField(db_column=u'Nombre de Usuario', primary_key=True, max_length=128)
    pass_field = models.CharField(db_column=u'Contraseña', max_lenght=128)
    namePrivilege = models.ForeignKey(Privilege, db_column=u'Privilegio')
        
    class Meta:
        managed = False
        db_table = 'Usuario'
        
class ActiveUser(models.Model):
    idActiveUser = models.AutoField(db_column=u'ID del usuario', primary_key=True)
    ipSurfer = models.CharField(db_column=u'IP del usuario activo', blank=True, max_lenght=15)
    nameSurfer = models.ForeignKey(Surfer, db_column=u'Usuario')
        
    class Meta:
        managed = False
        db_table = 'Usuarios Activos'
        
class Rule(models.Model):
    nameURL = models.CharField(db_column=u'Nombre de la URL', max_lenght=128, blank=True)
    idRule = models.AutoField(db_column=u'ID de la Regla', primary_key=True)
    isContent = models.BooleanField(db_column=u'Is content', blank=True)
    description = models.TextField(db_column=u'Descripcion de la Regla')
    allow = models.BooleanField(db_column=u'Permitido', blank=True)
    rFrom = models.DateTimeField(db_column=u'Desde')
    rTo = models.DateTimeField(db_column=u'Hasta')
        
    class Meta:
        managed = False
        db_table = 'Reglas'
    
class Content(models.Model):
    nameContent = models.CharField(db_column=u'Nombre del contenido', primary_key=True)
    urlList = models.TextField(db_column=u'Lista de urls')
        
    class Meta:
        managed = False
        db_table = 'Contenido'