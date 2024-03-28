# IMPORTING
# import internal libraries
from enum import Enum, auto

class GPTConnectionType(Enum):
    API = auto()
    LOCAL = auto()

class GPTEncodingType(Enum):
    OPENAI_GPT_3_1_2_TURBO = 'gpt-3.5-turbo'
    OPENAI_GPT_4 = 'gpt-4'

class GPTAPIEnvKeyType(Enum):
    OPENAI_API_ENV_KEY = 'OPENAI_API_KEY'