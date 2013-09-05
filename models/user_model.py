class User(object):
    
    
    def __init__(self, name, phone, email, organization):
        self.name = name
        self.phone = phone
        self.email = email
        self.organization = organization
        self.status = 'new'
        
        
    def activate(self):
        self.status = 'active'
        
    
    def suspend(self):
        self.status = 'suspended'
        
    
    def status(self):
        return self.status