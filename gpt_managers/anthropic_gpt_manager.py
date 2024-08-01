# IMPORTING
# importing internal libraries
from logging import Logger
import tiktoken
from anthropic import Anthropic
import os

# importing external libraries
from gpt_managers.gpt_manager import GPTManager
from enum_types.gpt_manager_types import GPTConnectionType, GPTModelType, GPTAPIEnvKeyType

class AnthropicAPIGPTManager(GPTManager):
    """
    A manager for the Anthropic API.

    Properties:
        gpt_connection_type: GPTConnectionType: Defines the type of connectivity of the GPT manager (API, LOCAL etc.)
        token_number_max: int: The maximum number of tokens that a summarization input is allowed to have
        gpt_encoding_type: GPTModelType: The encoding type that the model will use (eg. 'gpt-4'). USED ONLY TO APPROXIMATE WITH tiktoken
        gpt_model_type = GPTModelType: The model used for inference
        encoding: tiktoken.Encoding: The encoding type for the specific gpt_encoding_type
        logger: Logger: The basic logger available in the application
        client: any: The client interfacing with the GPT model

        venv_key: GPTAPIEnvKeyType: Defines what is the key to find the API Key in the .env store
    """

    gpt_connection_type: GPTConnectionType = GPTConnectionType.API
    token_number_max: int = 25000
    gpt_encoding_type: GPTModelType = GPTModelType.OPENAI_GPT_4_TURBO_PREVIEW
    gpt_model_type = GPTModelType = GPTModelType.ANTHROPIC_CLAUDE_3_OPUS
    encoding: tiktoken.Encoding
    logger: Logger
    client: Anthropic

    env_key: GPTAPIEnvKeyType = GPTAPIEnvKeyType.ANTHROPIC_API_ENV_KEY

    def __init__(self, logger: Logger) -> None:
        # pass the gpt model
        # main.py has already loaded the correct .env file
        api_key = os.getenv(self.env_key.value)
        self.client = Anthropic(
            api_key=api_key
        )

        # pass the logger
        self.logger = logger

        # get the correct encoding for the selected GPT model
        # WARNING: The use of the encoder here is a rough approximation of the tokens that will be used
        # Here we use OpenAI's tokenizer to get that rough approximation
        self.encoding = tiktoken.encoding_for_model(self.gpt_encoding_type.value)

    def __str__(self) -> str:
        """
        Returns a representation of the Anthropic API GPT Manager as a string.

        Returns:
            string: The GPT Manager representation as string
        """
        return 'Anthropic GPT API'

    def return_gpt_summary(self, to_summarize: str) -> str:
        """
        Returns the GPT summary of the provided prompt.

        Arguments:
            to_summarize: str: the data to summarize including any prompts
        """
        chat_completion = self.client.messages.create(
            model=self.gpt_model_type.value,
            max_tokens=self.token_number_max,
            messages=[
                {
                    'role': 'user',
                    'content': to_summarize
                }
            ]
        )
        print(chat_completion.content)
        return chat_completion.content

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
