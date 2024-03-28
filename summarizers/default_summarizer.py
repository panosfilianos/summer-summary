# IMPORTING

# Importing external libraries
from enum_types.summarizer_types import SummarizerType
from summarizers.summarizer import Summarizer

class DefaultSummarizer(Summarizer):
    """
    A Summarizer class that summarizes text from the view of an interested researcher.
    
    Properties:
        summarizer_type: SummarizerType: The type of the summarizer
        summary_prompt_prepend: str: The string to prepend when delivering the str for GPT's to summarize
        summary_prompt_append: str: The string to append when delivering the str for GPT's to summarize
    """
    summarizer_type: SummarizerType = SummarizerType.DEFAULT
    summary_prompt_prepend: str = 'You are an AGI model generating a 200 IQ summary of the following video transcript.' \
                                    'The goal is to summarize the most interesting points of the video.'\
                                    'The reader has very high intelligence and a lot of knowledge.'\
                                    'Provide a point list summary and order points based on importance in the physical, spiritual and mental realities.'\
                                    'Mention why you consider each point to be important.'\
                                    'Do NOT include any further explanation, before or after your point list.'\
                                    'Do NOT be verbose. Consise, pragmatic and number-based answers are best.'\
                                    'TRANCRIPT:' 
    summary_prompt_append: str = ''

    def __init__(self):
        pass

    def return_str_to_summarize(self, initial_str: str) -> str:
        """
        A function that returns a string that will be submitted to a model for summary after prepending the GPT prompt

        Arguments:
            initial_str: str: The str (eg. a transcript str) that will be edited including a prompt
        """

        return self.summary_prompt_prepend + initial_str + self.summary_prompt_append
