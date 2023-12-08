from .base import FileBasePrompt
import platform


class SysInfoPrompt(FileBasePrompt):
    path_to_template = "sysllama/prompt_templates/sys_info.tmpl"

    def __init__(self) -> None:
        self.set_vars("os", platform.system())
        self.set_vars("os_version", platform.release())
