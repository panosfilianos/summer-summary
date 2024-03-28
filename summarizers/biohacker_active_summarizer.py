# IMPORTING

# Importing external libraries
from enum_types.summarizer_types import SummarizerType
from summarizers.summarizer import Summarizer

class BiohackerActiveSummarizer(Summarizer):
    """
    A Summarizer class that summarizes text from the view of a biohacker.
    
    Properties:
        summarizer_type: SummarizerType: The type of the summarizer
        summary_prompt_prepend: str: The string to prepend when delivering the str for GPT's to summarize
        summary_prompt_append: str: The string to append when delivering the str for GPT's to summarize
    """
    summarizer_type: SummarizerType = SummarizerType.BIOHACKER_ACTIVE
    summary_prompt_prepend: str = 'You play the role of an active biohacker who has a very rigorous schedule who likes to process ' \
                                    ' a lot of concrete actions to further improve their longevity and live a more meaningful and full life.' \
                                     ' The goal is, as a human, to have the maximum lifespan and healthspan, exceeding the current average lifespan without injury.' \
                                    '. To do so, you need actionable, concrete information. For example, \'Drink more water\' is not concrete and is bad. \'Drink 2L of water per day\' is much better but do NOT include it if not in the transcript.'\
                                    'Read through the following transcript an make a markdown list of ALL actionable, concrete information provided in the transcript. ' \
                                    'Avoid words like \'regular\' and replace them with something concrete like: every 1 month, 1 year etc. Mention how often to do something with numbers.' \
                                    'Use product names in full and when mentioned notice how far along in the conversation the product is mentioned (eg. at 10 percent of the conversation).' \
                                    'For each item mention impact it may have on your longevity based on the transcript (eg. \'+++ heart health\' or  \'--- cancer risk\' etc. )Do NOT provide any other explanations. ' \
                                    'Do NOT leave the point vague. The high majority of markdown list points should include numerical data (eg. 2L, 2km, 2h etc.). TRANSCRIPT: '
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
