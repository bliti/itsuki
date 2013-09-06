####
# Receiver class.
# Named receiver because client would be confusing.
# The receiver is the person who we are calling on behalf of the user.
# User = emiter
# User's client = receiver
###


class Receiver(object):
    
    
    def __init__(self, user, name, phone, receiver_type):
        self.user = user           #user receiver belongs to.foreign key in DB.
        self.name = name
        self.phone = phone
        self.receiver_type = receiver_type  #associate, insured, etc.
        self.last_call = None
        self.status = 'suspended'
        
    def next_call(self, next_call_datetime):
        """ Date/time when next call is to be done. """
        self.next_call = next_call_datetime
        
    
    def last_call(self):
        return self.last_call
        
    
    def status(self, status):
        """
        Receiver status Active/Suspended. 
        Default is suspended, because we do not
        add to calling queue automatically.
        i.e. if active call, if not don't.
        """
        return self.status
        
        
    def activate(self):
        self.status = 'active'
        
        
    def suspend(self, status):
        self.status = 'suspended'