### IMPORTING
# Import external libraries
from dotenv import load_dotenv
import os


# Import internal libraries
from utils.arg_parser import ArgManager
from utils.basic_logger import basic_logger
from utils.worflow_manager import WorkflowManager

from data_managers.data_manager import DataManager
from summarizers.summarizer import Summarizer
from gpt_managers.gpt_manager import GPTManager


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

    workflow_manager = WorkflowManager()

    # get the YouTube data manager and fetch transcript
    data_manager: DataManager = workflow_manager.return_data_manager(args=arg_parser.args, logger=basic_logger)
    data = data_manager.fetch_data(source=arg_parser.args.url)
    
    # get summarizer
    summarizer = workflow_manager.return_summarizer(args=arg_parser.args)
    to_summarize = summarizer.return_str_to_summarize(initial_str=data)

    # get gpt manager
    gpt_manager = workflow_manager.return_gpt_manager(args=arg_parser.args, logger=basic_logger)
    token_number = gpt_manager.return_token_number(to_summarize=to_summarize)
    if (gpt_manager.valid_token_number(token_number=token_number)):
        gpt_manager.return_gpt_summary(to_summarize=to_summarize)
    else:
        basic_logger.error(token_number)
        return
    

if __name__ == "__main__":
    main()