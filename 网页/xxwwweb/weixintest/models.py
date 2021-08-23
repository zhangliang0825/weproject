# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cookies(models.Model):
    cookie_id = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cookies'


# class Data(models.Model):
#     objects = None
#     biz = models.CharField(max_length=30, blank=True, null=True)
#     title = models.CharField(max_length=200, blank=True, null=True)
#     html = models.TextField(blank=True, null=True)
#     link = models.CharField(max_length=1000, blank=True, null=True)
#     text = models.CharField(max_length=1000, blank=True, null=True)
#     media = models.CharField(max_length=30, blank=True, null=True)
#     author = models.CharField(max_length=30, blank=True, null=True)
#     is_top = models.CharField(max_length=30, blank=True, null=True)
#     is_ori = models.CharField(max_length=30, blank=True, null=True)
#     datetime = models.CharField(db_column='DATETIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     type = models.CharField(max_length=20, blank=True, null=True)
#
#     class Meta:
#         managed = True
#         db_table = 'data'

class Jianxiangdata(models.Model):
    objects = None
    post_id = models.IntegerField()
    content = models.TextField()
    class Meta:
        managed = True
        db_table = 'weixin_jj'


class Num(models.Model):
    num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'num'


class Words(models.Model):
    # id = models.IntegerField()
    word = models.CharField(unique=True, max_length=10)

    class Meta:
        managed = True
        db_table = 'words'

class Hisinfo_cx(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    media = models.CharField(max_length=30, blank=True, null=True)
    datetime = models.CharField(db_column='DATETIME', max_length=20, blank=True,
                                null=True)  # Field name made lowercase.
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hisinfo_cx'
