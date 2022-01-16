import os

from .base import *  # noqa: F401,F403

DEBUG = bool(os.getenv("DEBUG", True))

try:
    from .local import *  # noqa: F401,F403
except ImportError:
    pass
