def ble():
    return 5/0

try:
    ble()
except ZeroDivisionError:
    print ("division by zero 1")
except Exception:
    print ('Caught an exception')
finally:
    print ('In finally block for cleanup')



class MyError(Exception):
    """My own exception class

    Attributes:
        msg  -- explanation of the error
    """

    def __init__(self, msg):
        self.msg = msg

error = MyError("something wrong")
