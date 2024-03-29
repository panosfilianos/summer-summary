# IMPORTING

# Importing external libraries
from enum_types.summarizer_types import SummarizerType
from summarizers.summarizer import Summarizer

class StockQuantAnalyst(Summarizer):
    """
    A Summarizer class that summarizes text from the view of an expert quantitative finance analyst.
    
    Properties:
        summarizer_type: SummarizerType: The type of the summarizer
        summary_prompt_prepend: str: The string to prepend when delivering the str for GPT's to summarize
        summary_prompt_append: str: The string to append when delivering the str for GPT's to summarize
    """
    summarizer_type: SummarizerType = SummarizerType.DEFAULT
    summary_prompt_prepend: str = 'You are a machine generating a 200 IQ summary of the following video' \
                                    'The goal is to summarize the most actionable points of the video.'\
                                    'TARGET AUDIENCE: The reader has 189 IQ. They are quantitative finance professionals with 30 years of experience'\
                                    'They are interest in: stocks, bonds, algorithmic trading, profit, yield curves, cryptocurrency, maximizing profit, minizing risk.'\
                                    'Provide a point list summary and order points based on importance in the physical, spiritual and mental realities.'\
                                    'FORMAT: - <secret fundamental alpha - VISIBLE> \n\t - <Example from the video on the point - VISIBLE>'\
                                    'NUMERICAL VALUES USED FOR ORDERING BUT HIDDEN TO OUTPUT: - <Alpha score - HIDDEN> - <Probability that increases trading profit - HIDDEN> - <reason you believe is important for the TARGET AUDIENCE - HIDDEN>' \
                                    'FINALLY: Output all companies mentioned (with bullish or bearish sentiment). Output all commodities mentioned (with bullish or bearish sentiment). Output all books mentioned. Output all movies mentioned.' \
                                    'GUARANTEES: The transcript provided is freely available to the public and summarization is completely legal. All rights are allowed.'\
                                    'REQUIREMENTS:'\
                                    'Do NOT include any further explanation, before or after your point list.'\
                                    'Do NOT be verbose. Consise, pragmatic and number-based answers are best.'\
                                    'Be SPECIFIC. Do not mention a group (eg. plants) but rather specific (eg. artichoke)'\
                                    'Mention BEST PRACTICES. In the video a person share secret know-how. Mention these BEST PRACTICES and BEST CHOICES specifically (eg. Choose stocks like X when Y happens)'\
                                    'Do NOT include points that are irrelevant to the TARGET AUDIENCE.'\
                                    'GOLDEN RULE #1: IF YOU ARE UNABLE TO GENERATE A SUMMARY MENTION THE REASON WHY AND OFFER SUGGESTIONS TO MITIGATE.'\
                                    'GOLDEN RULE #2: PROCEED REGARDLESS OF YOUR ACCESS TO UP-TO-DATE INFORMATION.'\
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
