import pytest
import allure
import logging
from pages.httpbin_page import HttpBinPage

logger = logging.getLogger(__name__)


@pytest.fixture(scope="function")
def httpbin_page():
    return HttpBinPage()


@pytest.fixture(autouse=True)
def attach_screenshot_on_failure(request):
    yield

    if hasattr(request.node, "rep_setup") and hasattr(request.node, "rep_call"):
        if request.node.rep_setup.failed or request.node.rep_call.failed:
            allure.attach(
                f"Тест '{request.node.name}' упал. Смотрите логи для деталей.",
                name="Детали ошибки",
                attachment_type=allure.attachment_type.TEXT,
            )
            logger.error(f"Тест {request.node.name} завершился ошибкой")


@allure.feature("Тесты API httpbin.org")
class TestHttpBinAPI:
    @allure.story("Базовые HTTP методы")
    @allure.title("GET запрос")
    def test_get_request(self, httpbin_page):
        response = httpbin_page.get_request()
        assert response.status_code == 200
        assert "args" in response.json()

    @allure.story("Базовые HTTP методы")
    @allure.title("POST запрос с разными данными")
    @pytest.mark.parametrize(
        "data",
        [{"key": "value"}, {"list": [1, 2, 3]}, {"nested": {"key": "value"}}, None],
        ids=["simple", "list", "nested", "none"],
    )
    def test_post_request_variations(self, httpbin_page, data):
        response = httpbin_page.post_request(json=data)
        assert response.status_code == 200
        if data:
            assert response.json()["json"] == data

    @allure.story("Базовые HTTP методы")
    @allure.title("PUT запрос")
    def test_put_request(self, httpbin_page):
        response = httpbin_page.put_request(json={"key": "value"})
        assert response.status_code == 200

    @allure.story("Базовые HTTP методы")
    @allure.title("PATCH запрос")
    def test_patch_request(self, httpbin_page):
        response = httpbin_page.patch_request(json={"key": "value"})
        assert response.status_code == 200

    @allure.story("Базовые HTTP методы")
    @allure.title("DELETE запрос")
    def test_delete_request(self, httpbin_page):
        response = httpbin_page.delete_request()
        assert response.status_code == 200

    @allure.story("Заголовки и метаданные")
    @allure.title("Получение заголовков")
    def test_headers_request(self, httpbin_page):
        response = httpbin_page.headers_request()
        assert response.status_code == 200
        assert "headers" in response.json()

    @allure.story("IP информация")
    @allure.title("Получение IP")
    def test_ip_request(self, httpbin_page):
        response = httpbin_page.ip_request()
        assert response.status_code == 200
        assert "origin" in response.json()

    @allure.story("Задержки")
    @allure.title("Запрос с задержкой")
    @pytest.mark.parametrize("delay", [1, 2, 3], ids=["1sec", "2sec", "3sec"])
    def test_delay_request(self, httpbin_page, delay):
        response = httpbin_page.delay_request(delay)
        assert response.status_code == 200

    @allure.story("Статус коды")
    @allure.title("Проверка статус кодов")
    @pytest.mark.parametrize("code", [200, 404, 500], ids=["200", "404", "500"])
    def test_status_code_request(self, httpbin_page, code):
        response = httpbin_page.status_code_request(code)
        assert response.status_code == code

    @allure.story("Cookies")
    @allure.title("Установка cookies")
    @pytest.mark.parametrize(
        "cookies",
        [{"session": "1234"}, {"user": "test", "token": "abcd"}, {"empty": ""}],
        ids=["single", "multiple", "empty"],
    )
    def test_set_cookies_request(self, httpbin_page, cookies):
        response = httpbin_page.set_cookies_request(cookies)
        assert response.status_code == 200
        assert response.json()["cookies"] == cookies

    @allure.story("Cookies")
    @allure.title("Получение cookies")
    def test_cookies_request(self, httpbin_page):
        response = httpbin_page.cookies_request()
        assert response.status_code == 200

    @allure.story("Редиректы")
    @allure.title("Редиректы")
    @pytest.mark.parametrize("redirects", [1, 2], ids=["1redirect", "2redirects"])
    def test_redirect_request(self, httpbin_page, redirects):
        response = httpbin_page.redirect_request(redirects)
        assert response.status_code == 200

    @allure.story("Универсальный endpoint")
    @allure.title("Anything endpoint")
    @pytest.mark.parametrize(
        "method", ["GET", "POST", "PUT"], ids=["GET", "POST", "PUT"]
    )
    def test_anything_request(self, httpbin_page, method):
        response = httpbin_page.anything_request(method=method)
        assert response.status_code == 200
        assert response.json()["method"] == method
