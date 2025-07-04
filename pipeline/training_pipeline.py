from src.data_ingestion import DataIngestion
from utils.common_functions import *
from config.paths_config import *
from src.data_processing import DataProcessor
from src.model_training import ModelTraining

if __name__=="__main__":
    ## 1. Data Ingestion

    data_ingestion = DataIngestion(read_yaml(CONFIG_PATH))
    data_ingestion.run()

    ## 2 Data Processing 
    processor = DataProcessor(train_path=TRAIN_FILE_PATH,test_path=TEST_FILE_PATH,processed_dir=PROCESSED_DIR,config_path=CONFIG_PATH)
    processor.process()

    ## 3. Model Training 
    trainer = ModelTraining(PROCESSED_TRAIN_DATA_PATH,PROCESSED_TEST_DATA_PATH,MODEL_OUPUT_PATH)
    trainer.run()
