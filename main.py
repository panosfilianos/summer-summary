### IMPORTING
# Import external libraries

# Import internal libraries
from utils.arg_parser import ArgManager
from utils.basic_logger import basic_logger
from data_managers.youtube_manager import YouTubeManager
from summarizers.biohacker_active_summarizer import BiohackerActiveSummarizer


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

    # testing
    # get the YouTube data manager and fetch transcript
    youtube_manager = YouTubeManager(logger=basic_logger)
    data = youtube_manager.fetch_data(source=arg_parser.args.url)
    
    # get summarizer
    biohacker_summarizer = BiohackerActiveSummarizer()
    print(biohacker_summarizer.return_str_to_summarize(initial_str=data))

    # 
    

if __name__ == "__main__":
    main()