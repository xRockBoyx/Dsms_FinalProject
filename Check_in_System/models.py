# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Activity(models.Model):
    location = models.CharField(max_length=50, blank=True, null=True)
    act_name = models.CharField(max_length=50, blank=True, null=True)
    act_date = models.DateField(primary_key=True)
    admin = models.ForeignKey('AdminList', models.DO_NOTHING, blank=True, null=True)
    attend_list = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activity'


class ActivityAttendList(models.Model):
    act_date = models.ForeignKey(Activity, models.DO_NOTHING, db_column='act_date')
    act = models.OneToOneField('ClubMember', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'activity_attend_list'
        unique_together = (('act', 'act_date'),)


class AdminList(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_date = models.ForeignKey(Activity, models.DO_NOTHING, db_column='admin_date', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_list'


class CheckinList(models.Model):
    checkin_id = models.AutoField(primary_key=True)
    checkin_date = models.ForeignKey(Activity, models.DO_NOTHING, db_column='checkin_date', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'checkin_list'


class ClubMember(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    deparement = models.CharField(max_length=50, blank=True, null=True)
    stu_id = models.CharField(primary_key=True, max_length=10)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    identity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'club_member'
