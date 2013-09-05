class Call(object):
    
    
    def __init__(self, emiter, receiver):
        self.emiter = emiter
        self.receiver = receiver
        
        
    def dial_datetime(self, datetime):
        """ datetime of when call was dialed """
        self.datetime = datetime
        
    
    def result(self, result):
        """ Was called answered ? yes, no, voicemail """
        self.result = result
        
        
    def script(self, script):
        """ Script of call. i.e. the content of the call """
        self.script = script