from pydantic import BaseModel, HttpUrl, field_validator


class BrowseRequest(BaseModel):
    url: HttpUrl

    @field_validator("url")
    @classmethod
    def only_avito(cls, v: str) -> str:
        # Разрешаем только домены Авито
        if not any(d in v for d in ["avito.ru", "www.avito.ru", "m.avito.ru"]):
            raise ValueError("Only avito.ru URLs are allowed")

        return v


class BrowseResponse(BaseModel):
    status:  str
    message: str


__all__ = [
    'BrowseRequest',
    'BrowseResponse'
]
