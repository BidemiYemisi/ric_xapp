from ricxappframe.xapp_frame import RMRXapp
from abc import ABC

class _BaseManager(ABC):
    """
    Represents base Manager Abstract class
    Here initialize variables which will be common to all xapp

    Parameters:
        rmr_xapp: Reference to original RMRxappframe object
    """
    
    
    def __init__(self, rmr_xapp: RMRXapp):  # Constructor
        self._rmr_xapp = rmr_xapp
        self.logger = self._rmr_xapp.logger
        
        