class ZeroDeviceFound(Exception):
    """Raised when the device search returns with 0"""
    pass

class TooManyDevices(Exception):
    """Temporary exception until allow multiple devices feature implemented"""
    pass


# custom exceptions
# https://www.youtube.com/watch?v=hLLaw9BI-EE