from cifar10Project.config.configuration import ConfigurationManager
from cifar10Project.components.data_validation import DataValidation
from cifar10Project import logger


STAGE_NAME = "Data Validation stage"


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.validate_all_columns()
        except Exception as e:
            raise e


if __name__ == '__main__':
    try:
        logger.info('Wait before calling original main!!')
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========")
    except Exception as e:
        logger.exception(e)
        raise e
