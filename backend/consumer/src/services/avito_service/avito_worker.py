import time

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.common.exceptions import TimeoutException, WebDriverException

from src import config, get_logger


logger = get_logger("consumer.worker")


def get_driver() -> webdriver.Remote:
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--lang=ru-RU")
    chrome_options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/127.0.0.0 Safari/537.36'
    )
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_prefs = {
        "intl.accept_languages": "ru-RU,ru",
    }
    chrome_options.add_experimental_option("prefs", chrome_prefs)

    driver = webdriver.Remote(
        command_executor=f"{config.SELENIUM_HUB_URL}",
        options=chrome_options,
    )

    driver.set_page_load_timeout(config.PAGE_LOAD_TIMEOUT)
    driver.set_script_timeout(config.SCRIPT_TIMEOUT)

    return driver


def fetch_html(url: str) -> str:
    driver = None
    try:
        driver = get_driver()
        logger.info(f"Opening URL: {url}")
        driver.get(url)

        time.sleep(2.0)

        html = driver.page_source
        logger.info(f"Fetched HTML length: {len(html)}")
        return html

    except TimeoutException:
        logger.error("Page load timeout")
        return ""

    except WebDriverException as e:
        logger.exception(f"WebDriver error: {e}")
        return ""

    except Exception as e:
        logger.exception(f"Unknown error: {e}")
        return ""

    finally:
        if driver:
            driver.quit()


__all__ = [
    'fetch_html',
]
