# IMPORTING
# importing internal libraries
from abc import ABC, abstractmethod

# importing external libraries
from enum_types.summarizer_types import SummarizerType

class Summarizer(ABC):
    """
    A Summarizer class handles the creation of a text to summarize, and feedback management on the summarization quality.

    We consider that prompting and quality assurance is the actual summarization work, whereas the GPT models will anyway provide a result,
    so our work to create the summary is focused on the prompt and quality checks.
    
    Properties:
        summarizer_type: SummarizerType: The type of the summarizer
        summary_prompt_prepend: str: The string to prepend when delivering the str for GPT's to summarize
        summary_prompt_append: str: The string to append when delivering the str for GPT's to summarize
    """
    summarizer_type: SummarizerType
    summary_prompt_prepend: str
    summary_prompt_append: str

    @abstractmethod
    def __str__(self) -> str:
        """
        Represents the Summarizer as a string
        
        Returns:
            str: The Summarizer representation as a string
        """

    @abstractmethod
    def return_str_to_summarize(self, initial_str: str) -> str:
        """
        A function that returns a string that will be submitted to a model for summary

        Arguments:
            initial_str: str: The str (eg. a transcript str) that will be edited including a prompt
        """
        pass