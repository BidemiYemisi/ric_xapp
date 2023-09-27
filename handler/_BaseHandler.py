from ricxappframe.xapp_frame import RMRXapp
from abc import ABC, abstractmethod


class _BaseHandler(ABC):
    """
    Represents base Abstract Handler class
    Here initialize variables which will be common to all xapp

    Parameters:
        rmr_xapp: Reference to original RMRxappframe object
        msgtype: Integer specifying messagetype
    """

    def __init__(self, rmr_xapp: RMRXapp, msgtype):
        self._rmr_xapp = rmr_xapp
        self.logger = self._rmr_xapp.logger
        self.msgtype = msgtype
        self._rmr_xapp.register_callback(self.request_handler, msgtype) # registers callback for a particular msg_type. I should not worry about summary and sbuf that request_handler method takes, its register_callback func that pass both varaibles to it and I can get both and use them within the request_handler method
        
    @abstractmethod
    def request_handler(self, rmr_xapp, summary, sbuf): # summary contains the PAYLOAD i.e {"policy_type_id":"2"} and maybe othet stuff. Its a dictionary type
        pass
    
        