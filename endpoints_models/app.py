from endpoints_models.characters.api import Character

from utils.client import Client


class StoreApp:
    """App."""

    def __init__(self, url: str):
        self.url = url
        self.client = Client
        self.character = Character(self)
