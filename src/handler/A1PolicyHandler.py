import json
from ricxappframe.xapp_frame import RMRXapp, rmr
from ..utils.constants import Constants
from ._BaseHandler import _BaseHandler


class A1PolicyHandler(_BaseHandler):
    
    def __init__(self, rmr_xapp: RMRXapp, msgtype):
        super().__init__(rmr_xapp, msgtype)


    def request_handler(self, summary, sbuf):
        # return super().request_handler(rmr_xapp, summary, sbuf)

        self._rmr_xapp.rmr_free(sbuf)

        try:
            # summary is a dict and it contains loads of things, here I am getting only the RMR_MS_PAYLOAD as dict (json encoded as bytes)
            request = json.loads(summary[rmr.RMR_MS_PAYLOAD])
            self.logger.debug("Testxapp.A1PolicyHandler.request_handler method says::  Handler processing received request for message type {0}".format(self.msgtype))
            self.logger.info("Testxapp.A1PolicyHandler.request_handler method says:: Received summary is {0}".format(summary))
            self.logger.info("Testxapp.A1PolicyHandler.request_handler method says:: Received sbuf is {0}".format(sbuf))
            
        except (json.decoder.JSONDecodeError, KeyError):
            
            self.logger.error("Testxapp.A1PolicyHandler.request_handler method says:: Handler failed to parse the request (i.e json.loads(summary[rmr.RMR_MS_PAYLOAD])")
            return


        if self.verifyPolicy(request):
            
            self.logger.info("Testxapp.A1PolicyHandler.request_handler method says:: Request passed verification and handler processed request: {}".format(request))
        
        else:
            
            self.logger.error("Testxapp.A1PolicyHandler.request_handler method says:: Request failed verification and handler did not process request: {}".format(request))
            return

        # Build response
        response = self.buildPolicyResp(request)

        # Send response with new message type
        self._rmr_xapp.rmr_send(json.dumps(response).encode(), Constants.A1_POLICY_RESP)
        self.logger.info("Testxapp.A1PolicyHandler.request_handler method says:: Response for received request sent. Response is {}".format(response))


    # check if one of the keys are in the request dict
    def verifyPolicy(self, request: dict):
        for i in ["policy_type_id", "operation", "policy_instance_id"]:
            if i not in request:
                return False
        return True


    def buildPolicyResp(self, request: dict):
        request["handler_id"] = "testxapp"  # self._rmr_xapp.config["xapp_name"]
        del request["operation"]
        request["status"] = "OK"
        return request
    