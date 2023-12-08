"""
Custom exceptions for sysllama project.
"""


class TemplateNotFoundError(FileNotFoundError):
    """
    Raised when a template file cannot be found.
    """

    def __init__(self, template_path) -> None:
        super().__init__(f"Unable to find a file with template at {template_path}")


class CacheFolderNotExists(Exception):
    """
    Raised when .sysllama directory is not present.
    """

    def __init__(
        self,
    ) -> None:
        super().__init__(
            ".sysllama file is not present.Please Provide config details for creation."
        )
