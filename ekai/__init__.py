"""
ekai-chat: AI pair programming in your terminal

This package is based on Aider (https://github.com/Aider-AI/aider),
an outstanding open-source AI pair programming tool created by Aider AI (https://aider.chat).
We are grateful to the Aider team for their excellent work, which forms the foundation of this project.
This fork maintains the original Apache 2.0 license while rebranding for our specific use case.
"""

from packaging import version

__version__ = "0.75.3.dev"
safe_version = __version__

try:
    from ekai._version import __version__
except Exception:
    __version__ = safe_version + "+import"

if type(__version__) is not str:
    __version__ = safe_version + "+type"
else:
    try:
        if version.parse(__version__) < version.parse(safe_version):
            __version__ = safe_version + "+less"
    except Exception:
        __version__ = safe_version + "+parse"

__all__ = [__version__]
