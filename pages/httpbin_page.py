from .base_page import BasePage
import allure


class HttpBinPage(BasePage):
    @allure.step("GET запрос")
    def get_request(self, endpoint="/get", params=None):
        return self._make_request("GET", endpoint, params=params)

    @allure.step("POST запрос")
    def post_request(self, endpoint="/post", data=None, json=None):
        return self._make_request("POST", endpoint, data=data, json=json)

    @allure.step("PUT запрос")
    def put_request(self, endpoint="/put", data=None, json=None):
        return self._make_request("PUT", endpoint, data=data, json=json)

    @allure.step("DELETE запрос")
    def delete_request(self, endpoint="/delete"):
        return self._make_request("DELETE", endpoint)

    @allure.step("PATCH запрос")
    def patch_request(self, endpoint="/patch", data=None, json=None):
        return self._make_request("PATCH", endpoint, data=data, json=json)

    @allure.step("Запрос заголовков")
    def headers_request(self):
        return self._make_request("GET", "/headers")

    @allure.step("Запрос IP")
    def ip_request(self):
        return self._make_request("GET", "/ip")

    @allure.step("Запрос User-Agent")
    def user_agent_request(self):
        return self._make_request("GET", "/user-agent")

    @allure.step("Запрос с задержкой")
    def delay_request(self, delay):
        return self._make_request("GET", f"/delay/{delay}")

    @allure.step("Запрос статус кода")
    def status_code_request(self, code):
        return self._make_request("GET", f"/status/{code}")

    @allure.step("Basic Auth запрос")
    def basic_auth_request(self, user, passwd):
        return self._make_request("GET", f"/basic-auth/{user}/{passwd}")

    @allure.step("Bearer Auth запрос")
    def bearer_auth_request(self, token):
        headers = {"Authorization": f"Bearer {token}"}
        return self._make_request("GET", "/bearer", headers=headers)

    @allure.step("Stream запрос")
    def stream_request(self, lines):
        return self._make_request("GET", f"/stream/{lines}")

    @allure.step("Запрос cookies")
    def cookies_request(self):
        return self._make_request("GET", "/cookies")

    @allure.step("Установка cookies")
    def set_cookies_request(self, cookies):
        return self._make_request("GET", "/cookies/set", params=cookies)

    @allure.step("Удаление cookies")
    def delete_cookies_request(self, names):
        if isinstance(names, str):
            names = [names]
        return self._make_request("GET", "/cookies/delete", params={"name": names})

    @allure.step("Редирект запрос")
    def redirect_request(self, n):
        return self._make_request("GET", f"/redirect/{n}")

    @allure.step("Универсальный запрос")
    def anything_request(self, method="GET", **kwargs):
        return self._make_request(method, "/anything", **kwargs)
