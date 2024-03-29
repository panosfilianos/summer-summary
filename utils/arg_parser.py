### IMPORTING
# Import external libraries
import argparse
from argparse import Namespace, ArgumentParser
import re
from logging import Logger
from dataclasses import dataclass

# Import internal libraries
from enum_types.gpt_manager_types import GPTAPIType
from enum_types.summarizer_types import SummarizerType

@dataclass
class Arguments():
    """
    A dataclass holding all argument data and default values

    Properties:
        api: GPTAPIType: Use the best GPT API from OpenAPI, Anthropic etc.
        os: boolean: Use the best open source GPT available locally
        url: string: The YouTube video link
        s: SummarizerType: The persona to summarize
    """
    api: GPTAPIType = GPTAPIType.OPENAI
    os: bool= False
    url: str = ''
    s: SummarizerType = SummarizerType.DEFAULT


class ArgManager():
    """
    The manager for any CLI arguments

    Properties:
        parser: ArgumentParser: The class instance parsing the args
        args: Namespace: An object holding any args
        logger: Logger: The app logger provided
        args: Arguments: A dataclass holding all the argument data
    """

    parser: ArgumentParser = argparse.ArgumentParser(description="A parser for the arguments of the main application")
    arg_namespace: Namespace = None
    logger: Logger = None

    args: Arguments = Arguments()

    def __init__(self, logger: Logger):
        """
        Initializes the ArgParser and sets the available flags

        Returns:
            ArgumentParser: The ArgParser instance.
        """
        self.parser.add_argument('--api', type=str, help='Use the best GPT API from OpenAPI, Anthropic etc')
        self.parser.add_argument('--os', action='store_true', help='Use the best open source GPT available locally')
        self.parser.add_argument('--url', type=str, help='The YouTube video link')
        self.parser.add_argument('--s', type=str, help='The persona to summarize')
        self.logger = logger


    def parse(self):
        """
        Parses the argumens from the CLI into the Namespace instance
        """
        self.arg_namespace = self.parser.parse_args()

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
        if not self.arg_namespace.url:
            self.logger.error('No URL provided')
            return False
        elif not re.match(youtube_url_regex_expr, self.arg_namespace.url):
            self.logger.error('The URL provided is not matched as a YouTube URL')
            return False
        else:
            return True
        

    def pass_args_to_vars(self):
        """
        Passes the args from the Namespace instance to separate variables.
        Should be called after the args have been validated to be valid.

        Returns:
            None
        """

        self.args.api = self.arg_namespace.api
        self.args.os = self.arg_namespace.os
        self.args.url = self.arg_namespace.url
        self.args.s = SummarizerType(self.arg_namespace.s)

