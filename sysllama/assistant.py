from .llms.ollama import OllamaLLM
from .config import SysllamaConfig
import os
from functools import cache, cached_property
import json
from typing import Union, Dict, Any
import chromadb
from .exceptions import CacheFolderNotExists


class OllamaAssistant:
    """
    OllamaAssistant is the class responsible for interaction.
    """

    _config: SysllamaConfig = None
    _llm: OllamaLLM = None
    _vector_client: chromadb.ClientAPI = None

    _path_to_dir: str = None

    def __init__(self, config: [Union[SysllamaConfig, dict]] = None) -> None:
        self._cached(config=config)

        self._llm = OllamaLLM(**self._config.model_dump())

    def _load_assistant_config(self, config: dict):
        return SysllamaConfig(**config)

    def _cached(self, config):
        if self._path_to_dir is None:
            self._create_folder()

        if config is None:
            config = self._load_config_json()

            self._config = self._load_assistant_config(config)

        if isinstance(config, dict):
            self._config = self._load_assistant_config(config=config)
        if isinstance(config, SysllamaConfig):
            self._config = config
            self._create_config_file()

        # self._config = self._load_config_json()

        self._load_vector_client()

    def _create_folder(self):
        folder_name = ".sysllama"
        user_home = os.path.expanduser("~")
        folder_path = os.path.join(user_home, folder_name)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            raise CacheFolderNotExists()

        self._path_to_dir = folder_path

    def _create_config_file(self):
        file_name = "sysllama.json"
        if self._path_to_dir is None:
            self._create_folder()

        data = self._config.model_dump()
        with open(os.path.join(self._path_to_dir, file_name), "w") as file:
            json.dump(data, file)

    def _load_config_json(self):
        file_path = os.path.join(self._path_to_dir, "sysllama.json")
        if not os.path.isfile(file_path):
            self._create_config_file()
        else:
            with open(file_path, "r") as file:
                data = json.load(file)

        return data

    def _load_vector_client(self):
        path_to_db = os.path.join(self._path_to_dir, "vectordb")
        if os.path.exists(path_to_db):
            self._vector_client = chromadb.PersistentClient(path=path_to_db)
        else:
            os.makedirs(path_to_db)
            self._vector_client = chromadb.PersistentClient(path=path_to_db)

    @property
    def get_config(self):
        return self._config.model_dump()

    @property
    def get_cache_folder_path(self):
        if self._path_to_dir is None:
            self._create_folder()
        return self._path_to_dir
