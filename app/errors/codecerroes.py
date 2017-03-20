class InvalidCharsetError(BaseException):
       def __init__(self, value):
           self.value = "Invalid charset when decode"
       def __str__(self):
           return repr(self.value)