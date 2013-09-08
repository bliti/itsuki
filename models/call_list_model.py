# -*- coding: utf-8 -*-


###
# self.receivers is a list of the unique ids columns of the receivers.
# Not names, because names may be repeated.
###


import datetime


class CallList(object):


    def __init__(self, user, list_name, receivers):
        self.user = user
        self.list_name = list_name
        self.receivers = receivers                   #list [] type
        self.date_created = datetime.datetime.now()
        
        
    def add_receiver(self, receiver):
        self.receivers.append(receiver)
        
    
    def delete_receiver(self, receiver):
        self.receivers.remove(receiver)
        
        
    def update_list_name(self, new_name):
        self.list_name = new_name