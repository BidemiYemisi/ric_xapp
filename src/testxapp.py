from os import getenv
from ricxappframe.xapp_frame import RMRXapp, rmr
from .utils.constants import Constants
from .manager.A1PolicyManager import A1PolicyManager
from .handler.A1PolicyHandler import A1PolicyHandler
from mdclogpy import Logger


class TestXapp:
    
    def __init__(self):
        self.fake_sdl = getenv("USE_FAKE_SDL", False)
        self._rmr_xapp = RMRXapp(default_handler = self._default_handler,
                                 config_handler = self._handle_config_change,
                                 rmr_port = 4500,
                                 post_init = self._post_init,
                                 use_fake_sdl = bool(self.fake_sdl))
        
        
    def _post_init(self):
        
        """
        Function that runs when xapp initialization is complete
        """
        Logger.debug("_post_init called")
        # Create an instance of A1PolicyManager and send A1 policy query

        
        
    def _handle_config_change(self, config):
        """
        Function that runs at start and on every configuration file change.
        """
        pass
    
    
    def _default_handler(self, summary, sbuf):
        """
        Function that processes messages for which no handler is defined. This is the default handler
        """
        
        self.logger.info("Testxapp.A1PolicyHandler.default_handler called for msg type = " + str(summary[rmr.RMR_MS_MSG_TYPE]))
        self.logger.info("Textxapp.A1PolicyHandler.default_handler called and says:: Received summary is {}".format(summary))
        self.rmr_free(sbuf)
        
    
    def createHandlers(self):
        """
        Function that creates all the handlers for RMR Messages
        """
        a1_mgr = A1PolicyManager(self._rmr_xapp)
        a1_mgr.startup()
        # Creates instances of classes with callback functions that respond to a specific msg type. 
        A1PolicyHandler(self._rmr_xapp, Constants.A1_POLICY_REQ) # NEED TO CHECK THIS OUT: if A1_POLICY_REQ equals A1_POLICY_QUERY, then the handler for that query will be called else the default handler will be called
       
        
    def start(self, thread = False):
        """
        This is a convenience function that allows this xapp to run in Docker
        for "real" (no thread, real SDL), but also easily modified for unit testing
        (e.g., use_fake_sdl). The defaults for this function are for the Dockerized xapp.
        """  
        self.createHandlers()
        self._rmr_xapp.run(thread)
     
        
    def stop(self):
        """
        can only be called if thread=True when started
        TODO: could we register a signal handler for Docker SIGTERM that calls this?
        """
        self._rmr_xapp.stop()
        