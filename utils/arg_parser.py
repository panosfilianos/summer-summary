### IMPORTING
# Import external libraries
import argparse
from argparse import Namespace, ArgumentParser
import re
from logging import Logger

class ArgParser():
    """
    The parser for any CLI arguments

    Properties:
        parser: ArgumentParser: The class instance parsing the args
        args: Namespace: An object holding any args
        logger: Logger: The app logger provided

    """

    parser: ArgumentParser = argparse.ArgumentParser(description="A parser for the arguments of the main application")
    args: Namespace = None
    logger: Logger = None

    def __init__(self, logger: Logger):
        """
        Initializes the ArgParser and sets the available flags

        Returns:
            ArgumentParser: The ArgParser instance.
        """
        self.parser.add_argument('--openai', action='store_true', help='Use the best GPT from OpenAPI')
        self.parser.add_argument('--os', action='store_true', help='Use the best open source GPT available locally')
        self.parser.add_argument('--url', type=str, help='The YouTube video link')
        self.parser.add_argument('--s', type=str, help='The persona to summarize')
        self.logger = logger


    def parse(self):
        """
        Parses the argumens from the CLI
        """
        self.args = self.parser.parse_args()

    def valid_args(self):
        """
        Ensures any args passed on the parser are valid. Checks the existance of any required args and ensures
        that the URL is in YouTube format

        Returns:
            bool: If the args are valid.

        Todo:
            * Require url.
            * Validate the url comes from YouTube with a regex.
        """
        youtube_url_regex_expr = r"(https?:\/\/)?(www\.)?(youtube\.com|youtu\.be)(\/watch\?v=).+"
        if not self.args.url:
            self.logger.error('No URL provided')
            return False
        elif not re.match(youtube_url_regex_expr, self.args.url):
            self.logger.error('The URL provided is not matched as a YouTube URL')
            return False
        else:
            return True
