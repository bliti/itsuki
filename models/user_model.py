class User(object):
    
    
    def __init__(self, name, phone, employer):
        self.name = name
        self.phone = phone
        self.employer = employer
        self.status = 'new'
        
        
    def activate(self):
        self.status = 'active'
        
    
    def suspend(self):
        self.status = 'suspended'
        
    
    def status(self):
        return self.status