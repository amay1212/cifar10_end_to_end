from src.cifar10Project import logger
from cifar10Project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

if __name__ == '__main__':
    logger.info("This is the first custom log!!")
    STAGE_NAME = "Data Ingestion stage"
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e