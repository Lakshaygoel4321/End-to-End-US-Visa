# from US_VISA.logger import logging
# from US_VISA.exception import USvisaException
# import sys

# #logging.info("welcome to our custom log")

# try:
#     a = 2/0

# except Exception as e:
#     raise USvisaException(e,sys)


from US_VISA.pipeline.training_pipeline import TrainPipeline

obj = TrainPipeline()
obj.run_pipeline()
