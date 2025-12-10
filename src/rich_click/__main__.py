"""
Entry-point module for the command line prefixer, called in case you use `python -m rich_click`.

Why does this file exist, and why `__main__`? For more info, read:
- https://www.python.org/dev/peps/pep-0338/
- https://docs.python.org/3/using/cmdline.html#cmdoption-m
"""

from __future__ import annotations

from rich_click.cli import main


import sys

if __name__ == "__main__":
    # main will run a Click command which will either exit or raise
    try:
        if sys.platform == "win32":
            # Handle legacy windows
            import colorama  # type: ignore[import-untyped]

            colorama.init()
        main()
    except UnicodeDecodeError as e:
        print(f"Error: {e} \n\n\n {dir(e)}")
        raise
