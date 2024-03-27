### IMPORTING
# Import external libraries
from logging import Logger
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter, Formatter


# Import internal libraries
from data_managers.data_manager import DataManager
from enum_types.data_manager_types import DataManagerFlowType

class YouTubeManager(DataManager):
    """
    The manager that fetches data to summarize from YouTube

    Properties:

    """

    data_manager_flow_type: DataManagerFlowType = DataManagerFlowType.IMPORT
    logger: Logger
    formatter: TextFormatter = TextFormatter()

    def __init__(self, logger):
        self.logger = logger

    def fetch_data(self, source) -> str:
        """
        Fetches a transcript from YouTube, places it on the data property and returns it

        Properties:
            source: str: The complete YouTube URL
        
        Returns:
            str: The transcript as string

        Todo:
            - Support playlists
            - Extract the YouTube ID with a func
        """

        # get the youtube video ID only
        # The YouTube ID is always 11 characters at the end of the YouTube strinf
        video_id = source[-11:]

        transcipt_object = YouTubeTranscriptApi.get_transcript(video_id)
        data_formatted: str = self.formatter.format_transcript(transcript=transcipt_object)
        self.data = data_formatted
        return self.data
    
    def return_data(self):
        """
        Returns the fetched YouTube transcript as a string

        Returns:
            data: str: The fetched YouTube transcript as a string
        """
        return self.data

    def upload_data(self, data, destination):
        """
        Uploads the data to YouTube.
        Not available
        """
        pass


