# -*- coding: utf-8 -*-

###
# Roles: user, and admin. Default is user.
# Status: active (can login), suspended (cannot login)
###


class User(object):
    
    
    def __init__(self, name, phone, email, organization, role='user'):
        self.name = name
        self.phone = phone
        self.email = email
        self.organization = organization
        self.status = 'suspended'
        self.role = role
        
        
    def activate(self):
        self.status = 'active'
        
    
    def suspend(self):
        self.status = 'suspended'
        
    
    def status(self):
        return self.status