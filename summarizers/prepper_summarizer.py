# IMPORTING

# Importing external libraries
from enum_types.summarizer_types import SummarizerType
from summarizers.summarizer import Summarizer

class PrepperSummarizer(Summarizer):
    """
    A Summarizer class that summarizes text from the view of a highly intelligent prepper.
    
    Properties:
        summarizer_type: SummarizerType: The type of the summarizer
        summary_prompt_prepend: str: The string to prepend when delivering the str for GPT's to summarize
        summary_prompt_append: str: The string to append when delivering the str for GPT's to summarize
    """
    summarizer_type: SummarizerType = SummarizerType.DEFAULT
    summary_prompt_prepend: str = 'You are an AGI model generating a 200 IQ summary of the following video.' \
                                    'The goal is to summarize the most actionable points of the video.'\
                                    'TARGET AUDIENCE: The reader has 189 IQ. They are interest in: off-grid living, prepping, family, self-relience, cryptocurrencies.'\
                                    'Provide a point list summary and order points based on importance in the physical, spiritual and mental realities.'\
                                    'FORMAT: - <general rule - VISIBLE> \n\t - <short summary of what relevant happened on the video - VISIBLE>'\
                                    'NUMERICAL VALUES USED FOR ORDERING BUT HIDDEN TO OUTPUT: - <PrepperImportanceRating(tm) score - HIDDEN> - <reason you believe is important for the TARGET AUDIENCE - HIDDEN>' \
                                    'FINALLY: Output all plants mentioned and when/how to plant these seeds. Output all books mentioned. Output all movies mentioned.' \
                                    'REQUIREMENTS:'\
                                    'Do NOT include any further explanation, before or after your point list.'\
                                    'Do NOT be verbose. Consise, pragmatic and number-based answers are best.'\
                                    'Be SPECIFIC. Do not mention a group (eg. plants) but rather specific (eg. artichoke)'\
                                    'Mention BEST PRACTICES. In the video a person share secret know-how. Mention these BEST PRACTICES and BEST CHOICES specifically (eg. Choose 1in vs 2in tubing for purpose X)'\
                                    'Do NOT include points that are irrelevant to the TARGET AUDIENCE.'\
                                    'TRANCRIPT:' 
    summary_prompt_append: str = ''

    def __init__(self):
        pass

    def __str__(self) -> str:
        """
        Represents the Prepper summarizer as a string
        
        Returns:
            str: The Summarizer representation as a string
        """
        return 'Prepper'

    def return_str_to_summarize(self, initial_str: str) -> str:
        """
        A function that returns a string that will be submitted to a model for summary after prepending the GPT prompt

        Arguments:
            initial_str: str: The str (eg. a transcript str) that will be edited including a prompt
        """

        return self.summary_prompt_prepend + initial_str + self.summary_prompt_append
