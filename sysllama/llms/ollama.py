from sysllama.config import SysllamaConfig
from typing import Optional, Dict, Any
from sysllama.constants import DEFAULT_TEMPARATURE, DEFAULT_TOP_K, DEFAULT_TOP_P
from sysllama.scripts.dependencies import import_dependencies


class OllamaLLM:
    """
    OllamaLLM is base class to interact with Ollama instance server.
    """

    _config: SysllamaConfig = None

    def __init__(
        self,
        model: str,
        base_url: str = "http://localhost:11434",
        temperature: float = DEFAULT_TEMPARATURE,
        stream: bool = False,
        top_k: int = DEFAULT_TOP_K,
        top_p: float = DEFAULT_TOP_P,
        additional_kwargs: Optional[Dict[str, Any]] = {},
        **kwargs,
    ) -> None:
        self._config = SysllamaConfig(
            base_url=base_url,
            stream=stream,
            model=model,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p,
            cached=True,
        )

        self.additional_kwargs = additional_kwargs

    @classmethod
    def class_name(cls) -> str:
        return "OllamaLLM"

    @property
    def _model_kwargs(self) -> Dict[str, Any]:
        base_kwargs = {
            "temperature": self._config.temperature,
            "top_k": self._config.top_k,
            "top_P": self._config.top_p,
            "stream": self._config.stream,
        }
        return {**base_kwargs, **self.additional_kwargs}

    def _get_all_kwargs(self, **kwargs: Any) -> Dict[str, Any]:
        return {**self._model_kwargs, **kwargs}

    def generate(self, prompt: str, **kwargs: Any):
        requests = import_dependencies("requests")
        all_kwargs = self._get_all_kwargs(**kwargs)
        response = requests.post(
            url=f"{self._config.base_url}/api/generate",
            headers={"Content-Type": "application/json"},
            json={"prompt": prompt, "model": self._config.model, **all_kwargs},
        )
        response.encoding = "utf-8"
        if response.status_code != 200:
            optional_details = response.json().get("error")
            raise ValueError(
                f"Ollama call failed with status code {response.status_code}"
                f"Details : {optional_details}"
            )

        return response

    def ping(self, **kwargs):
        requests = import_dependencies("requests")
        response = requests.get(
            url=f"{self._config.base_url}",
        )
        response.encoding = "utf-8"
        if response.status_code != 200:
            optional_details = response.json().get("error")
            raise ValueError(
                f"Ollama call failed with status code {response.status_code}",
                f"Details : {optional_details}" f"Check if ollama is installed or not.",
            )

    def tags(self):
        requests = import_dependencies("requests")
        response = requests.get(
            url=f"{self._config.base_url}/api/tags",
        )
        response.encoding = "utf-8"
        if response.status_code == 200:
            result = response.json()
            return result
        else:
            optional_details = response.json().get("error")
            raise ValueError(
                f"Ollama call failed with status code {response.status_code}",
                f"Details : {optional_details}" f"Check if ollama is installed or not.",
            )

    def embeddings(self, prompt: str):
        requests = import_dependencies("requests")
        response = requests.post(
            url=f"{self._config.base_url}/api/embeddings",
            headers={"Content-Type": "application/json"},
            json={"prompt": prompt, "model": self._config.model},
        )
        response.encoding = "utf-8"
        if response.status_code == 200:
            result = response.json()
            return result
        else:
            optional_details = response.json().get("error")
            raise ValueError(
                f"Ollama call failed with status code {response.status_code}",
                f"Details : {optional_details}" f"Check if ollama is installed or not.",
            )
