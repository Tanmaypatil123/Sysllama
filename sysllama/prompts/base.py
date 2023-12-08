from abc import ABC, abstractmethod
import os
import sys
from typing import Dict
from sysllama.exceptions import TemplateNotFoundError
from pathlib import Path


class BasePrompt(ABC):
    """
    Base class for implementations of prompt.
    """

    _vars: Dict[str, str] = {}

    def set_vars(self, key, value):
        """
        set particular variable in prompt for formating.
        """
        self._vars[key] = value

    def get_var(self, key):
        """
        get the particular variable from prompt.
        """
        return self._vars.get(key, "This key is not present in prompt.")

    @property
    @abstractmethod
    def load_template(self) -> str:
        pass

    def format(self) -> str:
        template = self.load_template()
        return template.format(**self._vars)

    def template(self):
        return self.format()


class FileBasePrompt(BasePrompt):
    """
    Base File prompt template class to load file.
    """

    path_to_template: str = None

    def load_template(self) -> str:
        if os.path.exists(self.path_to_template):
            with open(self.path_to_template, "r") as file:
                template = file.read()

        else:
            raise TemplateNotFoundError(self.path_to_template)
        return template
