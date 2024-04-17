import sys
from industry.exception import IndustryException
from industry.pipeline.training_pipeline import TrainPipeline

try:
    train_pipeline = TrainPipeline()
    train_pipeline.run_pipeline()
except Exception as e:
    raise IndustryException(e, sys) from e