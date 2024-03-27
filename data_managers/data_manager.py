### IMPORTING
# Import external libraries
from logging import Logger
from abc import ABC, abstractmethod

# Import internal libraries
from enum_types.data_manager_types import DataManagerFlowType


class DataManager(ABC):
    """
    An abstract class used from all DataManagers.
    It defines the standard format of a DataManager

    Properties:
        data_manager_flow_type: DataManagerFlowType: If the manager supports downloading, uploading of data or both
        logger: Logger: The app logger provided
        data: str: The large string to summarize
    """

    data_manager_flow_type: DataManagerFlowType
    logger: Logger
    data: str

    @abstractmethod
    def fetch_data(self, source):
        """
        Fetches the data from the DataManager

        Properties:
            source: str: The source where the data is (eg. a YouTube URL)
        """
        pass


    @abstractmethod
    def return_data(self):
        """
        Returns the data of the DataManager

        Returns:
            data: Of any appropriate data type (usually str)
        """
        pass

    @abstractmethod
    def upload_data(self, data, destination):
        """
        Uploads the data of the DataManager

        Properties:
            destination: str: The destination where the data should be placed (eg. an Obsidian .md document)
        """
        pass
