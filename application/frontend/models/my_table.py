#!/usr/bin/env python
#coding=utf-8

from django.db import models

###############################################################################
# Here, define table model
###############################################################################
class My_table(models.Model):
    class Meta:
        db_table = 'user'

    # static var
    Enum_Sex = ('0', '1')

    my_id = models.AutoField(primary_key = True)
    my_name = models.CharField(max_length = 20, unique = True)
    my_age = models.IntegerField()
    my_sex = models.CharField(max_length = 1, choices = Enum_Sex)
    my_sign = models.TextField()

    def __unicode__(self):  # just use get table obj
        return self.my_name
###############################################################################
class Message(models.Model):
    class Meta:
        db_table = 'message'

    msg_id = models.AutoField(primary_key = True)
    msg_user_id = models.IntegerField()
    msg_usered_id = models.IntegerField()
    msg_content = models.TextField(blank = True)
    msg_date = models.DateTimeField()

    def __unicode__(self):
        return self.msg_id
###############################################################################
# Here, define table model functions
###############################################################################
class My_my_table():
    def __init__(self):
        pass

    def get_user_name_by_id_list(self, user_id_list = 0):
        if user_id_list:
            query = My_table.objects.filter(my_id__in = user_id_list).values('my_id', 'my_name')
            if query:
                return query
        return False

    def live_message(self, user_id = 0, usered_id = 0, content = '', date = ''):
        if user_id > 0 and usered_id > 0 and content and date:
            new_msg = Message(msg_user_id = user_id, msg_usered_id = usered_id, msg_content = content, msg_date = date)
            new_msg.save()
            return True
        return False

    def get_all_msg(self):
        query = Message.objects.all()
        ret = query.values('msg_id', 'msg_user_id', 'msg_usered_id', 'msg_content', 'msg_date')
        # print str(type(ret[0]['msg_date']))
        # print ret[0]['msg_date'].strftime('%Y-%m-%d %H:%M:%S')
        return ret

    def get_by_id(self, id = 0):
        if id > 0:
            query = My_table.objects.filter(my_id = id)
            if query:
                return query.values('my_id', 'my_name', 'my_age', 'my_sex', 'my_sign')
        return False

    def get_all(self):
        query = My_table.objects.all()
        return query.values('my_id', 'my_name', 'my_age', 'my_sex', 'my_sign')

    def insert_one(self, name = '', age = '0', sex = '0', sign = ''):
        if name and age and sex and sign:
            new_table_obj = My_table(my_name = name, my_age = age, my_sex = sex, my_sign = sign)
            new_table_obj.save()
            return True
        return False

    def delete_one(self, id = 0):
        if id > 0:
            query = My_table.objects.filter(my_id = id)
            if query:
                query.delete()
                return True
        return False

    def update_one(self, id = 0, name = ''):
        if id > 0 and name:
            query = My_table.objects.filter(my_id = id)
            ret_count = query.update(my_name = name)
            if ret_count > 0:
                return True
        return False

    def has_one(self, id = 0):
        if id > 0:
            try:
                query = My_table.objects.get(my_id = id)
                if query:
                    return True
            except My_table.DoesNotExist:
                return False
        return False

    def has_one_by_name(self, name = ''):
        if name > 0:
            try:
                query = My_table.objects.filter(my_name = name)
                if query:
                    return True
            except My_table.DoesNotExist:
                return False
        return False
###############################################################################
