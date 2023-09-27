import json
from ricxappframe.xapp_frame import RMRXapp, rmr
from ..utils.constants import Constants
from ._BaseHandler import _BaseHandler


class A1PolicyHandler(_BaseHandler):
    
    def __init__(self, rmr_xapp: RMRXapp, msgtype):
        super().__init__(rmr_xapp, msgtype)
        
        
    def request_handler(self, rmr_xapp, summary, sbuf):
        # return super().request_handler(rmr_xapp, summary, sbuf)
    
        self._rmr_xapp.rmr_free(sbuf)
        
        try:
            request = json.loads(summary[rmr.RMR_MS_PAYLOAD]) # summary is a dict and it contains loads of things, here I am getting only the RMR_MS_PAYLOAD as dict (json encoded as bytes)
            self.logger.debug("A1PolicyHandler.request_handler method says::  Handler processing received request for message type {0}".format(self.msgtype))
            self.logger.info("A1PolicyHandler.request_handler method says:: Received summary is {0}".format(summary))
        except (json.decoder.JSONDecodeError, KeyError):
            self.logger.error("A1PolicyHandler.request_handler method says:: Handler failed to parse the request (i.e json.loads(summary[rmr.RMR_MS_PAYLOAD])")
            return
        

        