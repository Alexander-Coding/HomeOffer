from src import get_logger
from src.core import broker, queue, exchange

from .avito_worker import fetch_html


logger = get_logger("consumer.main")


@broker.subscriber(queue=queue, exchange=exchange)
async def handle_browse_task(msg: dict):
    url = msg.get("url")

    if not url:
        logger.warning("Received message without 'url'")
        return

    logger.info(f"Received task: {url}")
    html = fetch_html(url)

    if html:
        logger.info(f"HTML BEGIN for {url}\n{html}\nHTML END")

    else:
        logger.warning(f"No HTML content fetched for {url}")
