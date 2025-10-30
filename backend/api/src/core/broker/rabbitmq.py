from faststream import FastStream
from faststream.rabbit import RabbitBroker, RabbitExchange, RabbitQueue, ExchangeType

from src import config, get_logger


logger = get_logger("api.queue")


broker = RabbitBroker(config.rabbitmq_url_amqp)
app_stream = FastStream(broker)


exchange = RabbitExchange(
    config.EXCHANGE_NAME,
    type=ExchangeType.TOPIC,
    durable=True,
)

queue = RabbitQueue(
    config.QUEUE_NAME,
    durable=True,
    routing_key=config.ROUTING_KEY,
)


async def start_rabbitmq() -> None:
    """Настройка обменников и очередей RabbitMQ."""
    await app_stream.start()

    await broker.declare_exchange(exchange)
    await broker.declare_queue(queue)

    logger.info("RabbitMQ setup completed.")


async def stop_rabbitmq() -> None:
    """Остановка подключения к RabbitMQ."""
    await app_stream.stop()

    logger.info("RabbitMQ connection closed.")


__all__ = [
    'app_stream',
    'start_rabbitmq',
    'stop_rabbitmq',
    'broker'
]
