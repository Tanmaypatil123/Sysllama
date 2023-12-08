import importlib


def import_dependencies(
    name: str,
    errors: str = "raise",
):
    assert errors in {"warn", "raise", "ignore"}

    msg = f"Missing dependency '{name}'." f"Use pip , conda or poetry to install {name}"

    try:
        module = importlib.import_module(name=name)
    except ImportError as exc:
        if errors == "raise":
            raise ImportError(msg) from exc
        return None

    return module
