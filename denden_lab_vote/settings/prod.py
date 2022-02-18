from .base import *  # noqa: F401,F403

try:
    from .local import *  # noqa: F401,F403
except ImportError:
    pass

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django": {"handlers": ["console"], "level": "INFO"},
    },
}
CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = ['https://denden-lab-vote.tk']