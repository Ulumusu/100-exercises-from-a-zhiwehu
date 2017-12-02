class MyError(Exception):
    """My own exception class

    Atributes:
        msg -- explanation of the error
    """

    def __init__(self, msg):
        self.msg=msg

error= MyError("something wrong")        
