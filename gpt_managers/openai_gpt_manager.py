# IMPORTING
# importing internal libraries
from logging import Logger
import tiktoken
from openai import OpenAI
import os
import pprint

# importing external libraries
from gpt_managers.gpt_manager import GPTManager
from enum_types.gpt_manager_types import GPTConnectionType, GPTEncodingType, GPTAPIEnvKeyType

class OpenAIAPIGPTManager(GPTManager):
    """
    A manager for the OpenAI API.

    Properties:
        gpt_connection_type: GPTConnectionType: Defines the type of connectivity of the GPT manager (API, LOCAL etc.)
        token_number_max: int: The maximum number of tokens that a summarization input is allowed to have
        gpt_encoding_type: GPTEncodingType: The encoding type that the model will use (eg. 'gpt-4')
        encoding: tiktoken.Encoding: The encoding type for the specific gpt_encoding_type
        logger: Logger: The basic logger available in the application
        client: any: The client interfacing with the GPT model

        venv_key: GPTAPIEnvKeyType: Defines what is the key to find the API Key in the .env store
    """

    gpt_connection_type: GPTConnectionType = GPTConnectionType.API
    token_number_max: int = 5000
    gpt_encoding_type: GPTEncodingType = GPTEncodingType.OPENAI_GPT_3_1_2_TURBO
    encoding: tiktoken.Encoding
    logger: Logger
    client: OpenAI

    env_key: GPTAPIEnvKeyType = GPTAPIEnvKeyType.OPENAI_API_ENV_KEY

    def __init__(self, logger: Logger) -> None:
        # pass the gpt model
        # main.py has already loaded the correct .env file
        api_key = os.getenv(self.env_key.value)
        self.client = OpenAI(
            api_key=api_key
        )

        # pass the logger
        self.logger = logger

        # get the correct encoding for the selected GPT model
        self.encoding = tiktoken.encoding_for_model(self.gpt_encoding_type.value)

    def return_gpt_summary(self, to_summarize: str) -> str:
        """
        Returns the GPT summary of the provided prompt.

        Arguments:
            to_summarize: str: the data to summarize including any prompts
        """
        chat_completion = self.client.chat.completions.create(
            model=self.gpt_encoding_type.value,
            messages=[
                {
                    'role': 'user',
                    'content': to_summarize
                }
            ]
        )
        print(chat_completion.choices[0].message.content)
        # self.logger.error(chat_completion.choices[0].message.content)
        return chat_completion.choices[0].message.content

    def return_token_number(self, to_summarize: str) -> int:
        """
        Returns the calculated number of tokens for the data to summarize with the current model

        Arguments:
            to_summarize: str: the data to summarize including any prompts
        """
        return len(self.encoding.encode(to_summarize))

    def valid_token_number(self, token_number: int) -> bool:
        """
        Returns if the token number is valid

        Arguments:
            token_number: int: The calculated number of tokens for the data to summarize
        """
        if (token_number > self.token_number_max):
            self.logger.error(f'The token number of the data to summarize is larger than allowed ({token_number} > {self.token_number_max})')
            return False
        return True
