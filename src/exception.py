import sys 
import logging
# for checking exception handling using import logger
# import logger

def error_msg_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_msg = 'Error occured in python script [{0}] line no.[{1}] error msg [{2}]'.format(
    file_name,exc_tb.tb_lineno,str(error)
    )
    return error_msg

class CustomException(Exception):
    def __init__(self,error_msg,error_deatils:sys):
        super().__init__(error_msg)
        self.error_message = error_msg_detail(error_msg,error_detail=error_deatils)

    def __str__(self):
        return self.error_message
    

# if __name__ == "__main__":
#     try:
#         a = 1/0
#     except Exception as e:
#         logging.info("Divide by zero")
#         raise CustomException(e,sys)


