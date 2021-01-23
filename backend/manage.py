#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    django_env = "$DJANGO_ENVIRONMENT"
    django_settings_value = "backend.settings.local" if django_env.endswith("DJANGO_ENVIRONMENT") else django_env
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", django_settings_value)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
