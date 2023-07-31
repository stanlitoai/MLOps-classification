import os
import urllib.request as request
import zipfile
from src.cnnClassifier import logger
from src.cnnClassifier.utils.common import get_size
from src.cnnClassifier.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                self.config.source_URL,
                filename=self.config.local_data_file)
            
            logger.info(f"Downloaded {filename} with following info: \n  {headers}")
        else:
            logger.info(f"File {self.config.local_data_file} already exists")


    def extract_zip_file(self):
        """
        zip_file_path = str
        Extracts the zip file to the local_data_file directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)