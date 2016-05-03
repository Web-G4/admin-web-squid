from __future__ import unicode_literals

from django.db import models


class Activeuser(models.Model):
    idactiveuser = models.AutoField(db_column='idActiveUser', primary_key=True)  # Field name made lowercase.
    ipsurfer = models.IntegerField(db_column='ipSurfer', blank=True, null=True)  # Field name made lowercase.
    namesurfer = models.ForeignKey('Surfer', models.DO_NOTHING, db_column='nameSurfer', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ActiveUser'


class Content(models.Model):
    namecontent = models.CharField(db_column='nameContent', primary_key=True, max_length=30)  # Field name made lowercase.
    urllist = models.TextField(db_column='urlList', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Content'


class Privilege(models.Model):
    nameprivilege = models.CharField(db_column='namePrivilege', primary_key=True, max_length=20)  # Field name made lowercase.
    isblock = models.IntegerField(db_column='isBlock', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Privilege'


class Rule(models.Model):
    nameurl = models.CharField(db_column='nameURL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idrule = models.AutoField(db_column='idRule', primary_key=True)  # Field name made lowercase.
    iscontent = models.BooleanField(db_column='isContent', default=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    allow = models.BooleanField(default=True)
    rfrom = models.TimeField(db_column='rFrom', blank=True, null=True)  # Field name made lowercase.
    rto = models.TimeField(db_column='rTo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Rule'


class Rulelist(models.Model):
    privilegeasigned = models.ForeignKey(Privilege, models.DO_NOTHING, db_column='privilegeAsigned', blank=True, null=True)  # Field name made lowercase.
    ruleasigned = models.ForeignKey(Rule, models.DO_NOTHING, db_column='ruleAsigned')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RuleList'


class Surfer(models.Model):
    username = models.CharField(primary_key=True, max_length=20)
    pass_field = models.CharField(db_column='pass', max_length=20, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    nameprivilege = models.ForeignKey(Privilege, models.DO_NOTHING, db_column='namePrivilege')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Surfer'
