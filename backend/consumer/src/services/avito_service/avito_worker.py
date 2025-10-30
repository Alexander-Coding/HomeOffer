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

    caps = DesiredCapabilities.CHROME.copy()
    caps["se:recordVideo"] = False

    driver = webdriver.Remote(
        command_executor=f"{config.SELENIUM_HUB_URL}/wd/hub",
        options=chrome_options,
        desired_capabilities=caps
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
