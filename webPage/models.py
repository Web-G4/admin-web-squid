# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class ActiveUser(models.Model):
    idActiveUser = models.AutoField(db_column='idActiveUser', primary_key=True)  # Field name made lowercase.
    ipSurfer = models.CharField(db_column='ipSurfer', max_length=15, blank=True, null=True)  # Field name made lowercase.
    nameSurfer = models.ForeignKey('Surfer', models.DO_NOTHING, db_column='nameSurfer', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        verbose_name = 'Usuario Activo'
        verbose_name_plural = 'Usuarios Activos'
        db_table = 'ActiveUser'

    def __str__(self):
        return self.ipSurfer


class Content(models.Model):
    nameContent = models.CharField(db_column='nameContent', primary_key=True, max_length=128)  # Field name made lowercase.
    urlList = models.TextField(db_column='urlList', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        verbose_name = 'Contenido'
        verbose_name_plural = 'Contenidos'
        db_table = 'Content'

    def __str__(self):
        return self.nameContent


class Privilege(models.Model):
    namePrivilege = models.CharField(db_column='namePrivilege', primary_key=True, max_length=128)  # Field name made lowercase.
    isBlock = models.IntegerField(db_column='isBlock', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        verbose_name = 'Privilegio'
        verbose_name_plural = 'Privilegios'
        db_table = 'Privilege'

    def __str__(self):
        return self.namePrivilege


class Rule(models.Model):
    nameURL = models.CharField(db_column='nameURL', max_length=128, blank=True, null=True)  # Field name made lowercase.
    idRule = models.AutoField(db_column='idRule', primary_key=True)  # Field name made lowercase.
    isContent = models.IntegerField(db_column='isContent', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    allow = models.IntegerField(blank=True, null=True)
    rFrom = models.TimeField(db_column='rFrom', blank=True, null=True)  # Field name made lowercase.
    rTo = models.TimeField(db_column='rTo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Rule'
        verbose_name = 'Regla'
        verbose_name_plural = 'Reglas'

    def __str__(self):
        return self.nameURL


class RuleList(models.Model):
    privilegeAsigned = models.ForeignKey(Privilege, models.DO_NOTHING, db_column='privilegeAsigned', blank=True)  # Field name made lowercase.
    ruleAsigned = models.ForeignKey(Rule, models.DO_NOTHING, db_column='ruleAsigned', blank=True, null=True)  # Field name made lowercase.
    idRuleList = models.AutoField(db_column='idRuleList', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RuleList'
        verbose_name = 'Lista de Reglas'
        verbose_name_plural = 'Listas de Reglas'

    def __str__(self):
        return str(self.idRuleList)

class Surfer(models.Model):
    username = models.CharField(primary_key=True, max_length=128)
    passField = models.CharField(db_column='pass', max_length=128, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    namePrivilege = models.ForeignKey(Privilege, models.DO_NOTHING, db_column='namePrivilege')  # Field name made lowercase.

    class Meta:
        managed = False
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'Surfer'

    def __str__(self):
        return self.username
