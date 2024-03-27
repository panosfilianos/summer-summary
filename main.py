### IMPORTING
# Import external libraries

# Import internal libraries
from utils.arg_parser import ArgManager
from utils.basic_logger import basic_logger

def main():
    # define arg parser
    arg_parser = ArgManager(logger=basic_logger)

    # parse
    arg_parser.parse()

    # if arguments are invalid, abort
    if not arg_parser.valid_args():
        basic_logger.error('Arguments are not valid. Aborting...')
        exit()

    # 

if __name__ == "__main__":
    main()