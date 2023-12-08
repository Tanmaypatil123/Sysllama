from pydantic import BaseModel, Field
from sysllama.constants import DEFAULT_TOP_K, DEFAULT_TEMPARATURE, DEFAULT_TOP_P


class SysllamaConfig(BaseModel):
    base_url: str = Field(
        description="Base url the model is hosted under.",
        default="http://localhost:11434",
    )
    stream: bool = Field(description="stream paramter for one output.", default=False)
    model: str = Field(description="The Ollama model to use.")
    temperature: float = Field(
        default=DEFAULT_TEMPARATURE,
        description="The temperature to use for sampling.",
        gte=0.0,
        lte=1.0,
    )
    top_k: int = DEFAULT_TOP_K
    top_p: float = DEFAULT_TOP_P
    cached: bool = True
    # serper_api_key: str = Field(description="serper api key for interaction with web.")
