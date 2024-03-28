# IMPORTING
# importing internal libraries
from logging import Logger

# importing external libraries
from data_managers.data_manager import DataManager
from data_managers.youtube_manager import YouTubeManager

from gpt_managers.gpt_manager import GPTManager
from gpt_managers.openai_gpt_manager import OpenAIAPIGPTManager

from summarizers.summarizer import Summarizer
from summarizers.biohacker_active_summarizer import BiohackerActiveSummarizer
from summarizers.prepper_summarizer import PrepperSummarizer
from summarizers.default_summarizer import DefaultSummarizer

from enum_types.summarizer_types import SummarizerType

from utils.arg_parser import Arguments


class WorkflowManager():
    """
    It manages the workflow of the app by choosing the correct DataManager, GPTManager and Summarizers to perform
    the actions defined on the CLI args.
    """

    def return_data_manager(self, args: Arguments, logger: Logger) -> DataManager:
        """
        This function returns the correct data manager specified in the arguments

        Arguments:
            args: Arguments: The arguments defined in the CLI
            logger: Logger: The basic logger of the app

        Returns:
            DataManager: a data manager instance
        """
        return YouTubeManager(logger=logger)
    

    def return_summarizer(self, args: Arguments) -> Summarizer:
        """
        This function returns the correct summarizer specified in the arguments

        Arguments:
            args: Arguments: The arguments defined in the CLI

        Returns:
            Summarizer: a summarizer profile instance
        """
        if (args.s is SummarizerType.BIOHACKER_ACTIVE):
            return BiohackerActiveSummarizer()
        if (args.s is SummarizerType.PREPPER):
            return PrepperSummarizer()
        else:
            return DefaultSummarizer()
    
    def return_gpt_manager(self, args: Arguments, logger: Logger) -> GPTManager:
        """
        This function returns the correct GPT Manager specified in the arguments

        Arguments:
            args: Arguments: The arguments defined in the CLI
            logger: Logger: The basic logger of the app

        Returns:
            GPTManager: a GPTManager type instance
        """
        return OpenAIAPIGPTManager(logger=logger)
