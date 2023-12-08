from .base import FileBasePrompt


class OperationCheckPrompt(FileBasePrompt):
    path_to_template = "sysllama/prompt_templates/query_operation_check.tmpl"

    def __init__(self, prompt, **kwargs) -> None:
        self.set_vars("user_query", prompt)
        super().__init__(**kwargs)
