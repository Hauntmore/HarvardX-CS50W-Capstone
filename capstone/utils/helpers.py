"""
Reusable utility functions and helper methods to assist in executing various common operations and tasks throughout the project.
"""

import json
import os

from django.conf import settings


def load_configuration_file(
    path: str = os.path.join(settings.BASE_DIR, "..", "config.json")
):
    """
    A function that loads the config.json file and return its properties.

    Args:
        path (str): The path to the configuration file.

    Returns:
        dict: A dictionary containing the configuration data parsed from the file.

    Raises:
        FileNotFoundError: If the specified path does not exist.
        IOError: If there is an issue reading the file.

    Example:
        >>> contents = load_configuration_file('./path/to/config.json')
    """

    with open(path, "r", encoding="UTF-8") as file:
        contents = json.load(file)

    return contents
