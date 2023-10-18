from .testxapp import TestXapp

def launchXapp():
    testxapp = TestXapp()
    testxapp.start()
    
    
if __name__ == "__main__":
    launchXapp()