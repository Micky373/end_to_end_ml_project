import sys
import logging
import math

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()

    error_message = "Error occur in Python script name [{}] \
        line number [{}] error message [{}]".format(
            exc_tb.tb_frame.f_code.co_filename,
            exc_tb.tb_lineno,
            str(error)
        )
    

    return error_message

class CustomException(Exception):

    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail)

    
    def __str__(self) :
        return self.error_message



