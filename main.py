### IMPORTING
# Import external libraries
from dotenv import load_dotenv
import os


# Import internal libraries
from utils.arg_parser import ArgManager
from utils.basic_logger import basic_logger
from data_managers.youtube_manager import YouTubeManager
from summarizers.biohacker_active_summarizer import BiohackerActiveSummarizer
from gpt_managers.openai_gpt_manager import OpenAIAPIGPTManager


def main():
    # define arg parser
    arg_parser = ArgManager(logger=basic_logger)

    # parse
    arg_parser.parse()

    if not arg_parser.valid_args():
        # if arguments are invalid, abort
        basic_logger.error('Arguments are not valid. Aborting...')
        exit()
    else:
        # otherwise, pass them to the arguments object
        arg_parser.pass_args_to_vars()

    # load the .env
    dotenv_path = '.env'
    load_dotenv(dotenv_path=dotenv_path)

    # testing
    # get the YouTube data manager and fetch transcript
    youtube_manager = YouTubeManager(logger=basic_logger)
    data = youtube_manager.fetch_data(source=arg_parser.args.url)
    
    # get summarizer
    biohacker_summarizer = BiohackerActiveSummarizer()
    to_summarize = biohacker_summarizer.return_str_to_summarize(initial_str=data)

    # get gpt manager
    openai_gpt_manager = OpenAIAPIGPTManager(logger=basic_logger)
    token_number = openai_gpt_manager.return_token_number(to_summarize=to_summarize)
    if (openai_gpt_manager.valid_token_number(token_number=token_number)):
        openai_gpt_manager.return_gpt_summary(to_summarize=to_summarize)
    else:
        basic_logger.error(token_number)
        return
    

if __name__ == "__main__":
    main()