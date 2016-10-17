# Mon May 26 18:46:09 EEST 2014, nickkouk

class MyError(Exception):
    """Base class for exceptions in this module."""
    pass

class InputException(MyError):
    def __init__(self, value):
        self.value = value
        message = "kalimera_message"

    def __str__(self):
        return repr(self.value)

    # In case I need such kind of behaviour
    #def _get_message(self): 
        #return self._message
    #def _set_message(self, message): 
        #self._message = message

    #message = property(_get_message, _set_message)


# U it like "try move the plunger, except inputException("no more volume")
