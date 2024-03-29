# IMPORTING
# Importing internal libraries
from abc import ABC, abstractmethod
from logging import Logger

import tiktoken

# importing external libraries
from enum_types.gpt_manager_types import GPTConnectionType, GPTModelType

class GPTManager(ABC):
    """
    A class that manages any connection with a GPT. This can either be through API, or via connection to a local instance.

    Properties:
        gpt_connection_type: GPTConnectionType: Defines the type of connectivity of the GPT manager (API, LOCAL etc.)
        token_number_max: int: The maximum number of tokens that a summarization input is allowed to have
        gpt_encoding_type: GPTModelType: The encoding type that the model will use (eg. 'gpt-4')
        encoding: tiktoken.Encoding: The encoding type for the specific gpt_encoding_type
        logger: Logger: The basic logger available in the application
        client: any: The client interfacing with the GPT model
    """

    gpt_connection_type: GPTConnectionType
    token_number_max: int
    gpt_encoding_type: GPTModelType
    encoding: tiktoken.Encoding
    logger: Logger
    client: any

    @abstractmethod
    def return_gpt_summary(self, to_summarize):
        """
        Returns the GPT summary of the provided prompt.

        Arguments:
            to_summarize: the data to summarize including any prompts
        """
        pass


    @abstractmethod
    def return_token_number(self, to_summarize) -> int:
        """
        Returns the calculated number of tokens for the data to summarize

        Arguments:
            to_summarize: the data to summarize including any prompts
        """
        pass

    @abstractmethod
    def valid_token_number(self, token_number:int) -> bool:
        """
        Returns if the token number is valid

        Arguments:
            token_number: int: The calculated number of tokens for the data to summarize
        """
        pass

