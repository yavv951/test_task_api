from pydantic import BaseModel

from endpoints_models.characters.model import DataGetCharacter, DataCharacterInfo
from utils.logger import log

from utils.validator import Validator


class Character(Validator):
    """API endpoint post."""

    CHARACTERS = "/characters"
    CHARACTER = "/character"

    def __init__(self, app):
        self.app = app

    @log("GET characters")
    def get_characters(self, data: DataGetCharacter, type_response: BaseModel):
        """GET request."""
        response = self.app.client.request(
            method="GET",
            url=f"{self.app.url}{self.CHARACTERS}",
            auth=(data.username, data.password)
        )
        return self.structure(response, type_response=type_response)

    @log("GET character")
    def get_character(self, data: DataGetCharacter, type_response: BaseModel):
        """GET request."""
        response = self.app.client.request(
            method="GET",
            url=f"{self.app.url}{self.CHARACTER}?name={data.name}",
            auth=(data.username, data.password)
        )
        return self.structure(response, type_response=type_response)


    @log("POST character")
    def post_character(self, data: DataGetCharacter, data_ch: DataCharacterInfo, type_response=None):
        """Post request."""
        response = self.app.client.request(
            method="POST",
            url=f"{self.app.url}{self.CHARACTER}",
            json=data_ch.dict(),
            auth=(data.username, data.password)
        )
        return self.structure(response, type_response=type_response)

    @log("DELETE character")
    def delete_character(self, data: DataGetCharacter, type_response: BaseModel):
        """DELETE request."""
        response = self.app.client.request(
            method="DELETE",
            url=f"{self.app.url}{self.CHARACTER}?name={data.name}",
            auth=(data.username, data.password)
        )
        return self.structure(response, type_response=type_response)