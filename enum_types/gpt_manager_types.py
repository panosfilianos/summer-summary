# IMPORTING
# import internal libraries
from enum import Enum, auto

class GPTConnectionType(Enum):
    API = auto()
    LOCAL = auto()

class GPTAPIType(Enum):
    OPENAI = 'openai'
    ANTHROPIC = 'anthropic'

class GPTModelType(Enum):
    OPENAI_GPT_3_1_2_TURBO = 'gpt-3.5-turbo'
    OPENAI_GPT_4 = 'gpt-4'
    OPENAI_GPT_4_TURBO_PREVIEW = 'gpt-4-turbo-preview'
    ANTHROPIC_CLAUDE_3_OPUS = 'claude-3-opus-20240229'
    ANTHROPIC_CLAUDE_3_SONNET = 'claude-3-sonnet-20240229'
    ANTHROPIC_CLAUDE_3_HAIKU = 'claude-3-haiku-20240307'


class GPTAPIEnvKeyType(Enum):
    OPENAI_API_ENV_KEY = 'OPENAI_API_KEY'
    ANTHROPIC_API_ENV_KEY = 'ANTHROPIC_API_ENV_KEY'