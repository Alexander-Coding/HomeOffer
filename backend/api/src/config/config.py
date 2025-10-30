from pydantic_settings import BaseSettings


class Config(BaseSettings):
    RABBITMQ_USER: str
    RABBITMQ_PASS: str
    RABBITMQ_HOST: str
    RABBITMQ_PORT: int

    QUEUE_NAME:    str
    EXCHANGE_NAME: str
    ROUTING_KEY:   str
    
    LOG_LEVEL:     str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    @property
    def rabbitmq_url_amqp(self):
        """Получение ссылки на подключение к брокеру сообщений RabbitMQ через amqp (асинхронно)"""
        return f"amqp://{self.RABBITMQ_USER}:{self.RABBITMQ_PASS}@{self.RABBITMQ_HOST}:{self.RABBITMQ_PORT}"


config = Config()


__all__ = [
    'config'
]
