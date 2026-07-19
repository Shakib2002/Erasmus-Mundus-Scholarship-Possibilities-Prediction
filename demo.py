import sys
from scholarship_prediction.logger import logging
from scholarship_prediction.exception import ScholarshipException


try:
    raise Exception("This is a test exception")
except Exception as e:
    logging.info("This is a test log")
    raise ScholarshipException(e, sys)