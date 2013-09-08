# -*- coding: utf-8 -*-

###
# Call script. i.e what the receiver hears.
###

class Script(object):


    def __init__(self, user, script_title, script_body):
        self.user = user
        self.title = script_title
        self.body = script_body
        
        
    def update_script_body(self, new_script_body):
        self.body = new_script_body
        
        
    def update_script_title(self, new_script_title):
        self.body = new_script_title