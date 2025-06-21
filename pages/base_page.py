import requests
import allure
from allure_commons.types import AttachmentType
import logging

logger = logging.getLogger(__name__)


class BasePage:
    def __init__(self):
        self.base_url = "https://httpbin.org"
        self.session = requests.Session()

    def _make_request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"

        with allure.step(f"Выполнение {method} запроса к {url}"):
            try:
                response = self.session.request(method, url, **kwargs)
                logger.info(f"Запрос: {method} {url} - Статус: {response.status_code}")

                allure.attach(
                    f"Запрос:\n{method} {url}\nЗаголовки: {kwargs.get('headers', {})}\nТело: {kwargs.get('json', '')}",
                    name="Детали запроса",
                    attachment_type=AttachmentType.TEXT,
                )

                allure.attach(
                    f"Ответ:\nСтатус: {response.status_code}\nЗаголовки: {response.headers}\nТело: {response.text}",
                    name="Детали ответа",
                    attachment_type=AttachmentType.TEXT,
                )

                return response
            except Exception as e:
                logger.error(f"Ошибка при выполнении запроса: {str(e)}")
                allure.attach(
                    f"Ошибка запроса: {str(e)}",
                    name="Ошибка выполнения запроса",
                    attachment_type=AttachmentType.TEXT,
                )
                raise
