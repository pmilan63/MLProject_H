import sys
from src.mlproject.logger import logging

def error_message_detail(error, error_detail: sys):
    """
    Extracts the error message and details from an exception.
    
    Args:
        error (Exception): The exception object.
        detail (sys): The sys module to access exc_info.
    
    Returns:
        str: A formatted string containing the error message and details.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in script: [{file_name}] at line number: [{line_number}] with message: [{error}]"
    return error_message

class CustomException(Exception):
    """
    Custom exception class that formats error messages.
    
    Args:
        error (Exception): The exception object.
        error_detail (sys): The sys module to access exc_info.
    """
    
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)
    
    def __str__(self):
        return self.error_message

     