from os import getenv
from ricxappframe.xapp_frame import RMRXapp, rmr
from .utils.constants import Constants
from .manager.A1PolicyManager import A1PolicyManager
from .handler.A1PolicyHandler import A1PolicyHandler
from mdclogpy import Logger


testxapp = None       
        
def _post_init(self):
        
    """
    Function that runs when xapp initialization is complete
    """
    Logger.debug("Calling the post_init method in testxapp-python")

    # Create an instance of A1PolicyManager and send A1 policy query
    #a1_mgr = A1PolicyManager(testxapp)
    #a1_mgr.startup()
        
        
def _handle_config_change(self):
    """
    Function that runs at start and on every configuration file change.
    """
    pass
    
    
def _default_handler(self, summary, sbuf):
    """
    Function that processes messages for which no handler is defined. This is the default handler
    """
    
    Logger.info("Testxapp.A1PolicyHandler.default_handler called for msg type = " + str(summary[rmr.RMR_MS_MSG_TYPE]))
    Logger.info("Textxapp.A1PolicyHandler.default_handler called and says:: Received summary is {}".format(summary))
    self.rmr_free(sbuf)
    
    
""" def createHandlers(self):
   
     #Function that creates all the handlers for RMR Messages
   
    # Creates instances of classes with callback functions that respond to a specific msg type.
    Logger.info("Testxapp starting.......")
    global testxapp 
    fake_sdl = getenv("USE_FAKE_SDL", False)
    testxapp = RMRXapp(default_handler = _default_handler,
                       config_handler= _handle_config_change,
                       rmr_port=4560,
                       post_init=_post_init,
                       use_fake_sdl=bool(fake_sdl))
    Logger.info("Testxapp created .......")
    A1PolicyHandler(testxapp, Constants.A1_POLICY_REQ) # NEED TO CHECK THIS OUT: if A1_POLICY_REQ equals A1_POLICY_QUERY, then the handler for that query will be called else the default handler will be called
    a1_mgr = A1PolicyManager(testxapp)
    a1_mgr.startup() """
    
def start(thread = False):
    """
    This is a convenience function that allows this xapp to run in Docker
    for "real" (no thread, real SDL), but also easily modified for unit testing
    (e.g., use_fake_sdl). The defaults for this function are for the Dockerized xapp.
    """ 

    Logger.info("Testxapp is starting.......")
    global testxapp 
    fake_sdl = getenv("USE_FAKE_SDL", None)
    testxapp = RMRXapp(default_handler = _default_handler,
                       rmr_port=4560,
                       post_init=_post_init,
                       use_fake_sdl=bool(fake_sdl))
    Logger.debug("Testxapp created .......")
    A1PolicyHandler(testxapp, Constants.A1_POLICY_REQ) # NEED TO CHECK THIS OUT: if A1_POLICY_REQ equals A1_POLICY_QUERY, then the handler for that query will be called else the default handler will be called
    a1_mgr = A1PolicyManager(testxapp)
    a1_mgr.startup()

     #self.createHandlers()
    testxapp.run(thread)
    
    
def stop(self):
    """
    can only be called if thread=True when started
    TODO: could we register a signal handler for Docker SIGTERM that calls this?
    """
    testxapp.stop()
    