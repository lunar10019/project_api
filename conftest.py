import pytest
import allure
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def pytest_configure(config):
    config.option.allure_report_dir = (
        f"./allure-results/{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    )


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, f"rep_{rep.when}", rep)

    if rep.when == "call" and rep.failed:
        try:
            allure.attach(
                f"Тест {item.name} упал с ошибкой: {rep.longreprtext}",
                name="Детали ошибки",
                attachment_type=allure.attachment_type.TEXT,
            )
        except Exception as e:
            logger.error(f"Не удалось прикрепить детали ошибки: {str(e)}")
