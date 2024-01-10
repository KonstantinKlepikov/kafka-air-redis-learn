import toml
from typing import Type
from pydantic_settings import BaseSettings
from app.schemas import scheme_error


poetry_data = toml.load('pyproject.toml')['tool']['poetry']
ErrorType = dict[int, dict[str, Type[scheme_error.HttpErrorMessage]]]


class Settings(BaseSettings):

    # open-api settings
    API_V1: str = "/api/v1"
    title: str = poetry_data['name']
    descriprion: str = poetry_data['description']
    version: str = poetry_data['version']
    openapi_tags: list = [
        {
            "name": "files",
            "description": "Files api",
        },
    ]

    # open-api errors
    ERRORS: ErrorType = {
        400: {'model': scheme_error.HttpError400},  # type: ignore
        404: {'model': scheme_error.HttpError404},  # type: ignore
        409: {'model': scheme_error.HttpError409},  # type: ignore
            }


settings = Settings()
