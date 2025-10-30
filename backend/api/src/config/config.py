from pydantic_settings import BaseSettings


class Config(BaseSettings):
    RABBITMQ_USER: str
    RABBITMQ_PASS: str
    RABBITMQ_HOST: str
    RABBITMQ_PORT: int

    QUEUE_NAME:    str
    EXCHANGE_NAME: str
    ROUTING_KEY:   str

    SELENIUM_HUB_URL: str

    LOG_LEVEL:         str
    PAGE_LOAD_TIMEOUT: int
    SCRIPT_TIMEOUT:    int


config = Config()


__all__ = [
    'config'
]
