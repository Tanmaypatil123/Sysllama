from .base import FileBasePrompt
from .sys_info import SysInfoPrompt


class Mainprompt(FileBasePrompt):
    path_to_template = "sysllama/prompt_templates/main_prompt.tmpl"

    def __init__(self, prompt, **kwargs) -> None:
        sys_info_prompt = SysInfoPrompt()
        self.set_vars("sys_info", sys_info_prompt.template())
        self.set_vars("user_query", prompt)
        super().__init__(**kwargs)
