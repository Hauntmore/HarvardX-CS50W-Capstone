import json
import os

from django.conf import settings


def load_configuration_file():
    path = os.path.join(settings.BASE_DIR, "..", "config.json")

    with open(path, "r", encoding="UTF-8") as file:
        contents = json.load(file)

    return contents
