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

    @property
    def rabbitmq_url_amqp(self):
        """Получение ссылки на подключение к брокеру сообщений RabbitMQ через amqp (асинхронно)"""
        return f"amqp://{self.RABBITMQ_USER}:{self.RABBITMQ_PASS}@{self.RABBITMQ_HOST}:{self.RABBITMQ_PORT}"


config = Config()


__all__ = [
    'config'
]
