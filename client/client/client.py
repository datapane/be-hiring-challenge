import logging
from urllib.parse import urljoin

import requests

from client.constants import DEFAULT_TIMEOUT, DEFAULT_USER_AGENT
from client.exceptions import ClientRequestError


class APIClient:
    def __init__(
        self,
        base_url=None,
        token=None,
        timeout=DEFAULT_TIMEOUT,
        user_agent=DEFAULT_USER_AGENT,
        verify=False,
        logger=None,
    ):
        self.timeout = timeout
        self.user_agent = user_agent
        self.verify = verify
        self.base_url = base_url
        self.token = token
        self.logger = logger or logging.getLogger()

    def get(self, url) -> requests.Response:
        return self._request(url, "get")

    def post(self, url, payload=None, files=None) -> requests.Response:
        return self._request(url, "post", data=payload, files=files)

    def put(self, url, payload=None) -> requests.Response:
        return self._request(url, "put", data=payload)

    def patch(self, url, payload=None) -> requests.Response:
        return self._request(url, "patch", data=payload)

    def delete(self, url) -> requests.Response:
        return self._request(url, "delete")

    def _request(self, url, method, data=None, files=None) -> requests.Response:
        _url = urljoin(self.base_url, url)
        headers = {
            "user-agent": self.user_agent,
        }

        request = getattr(requests, method)
        params = {"url": _url, "headers": headers, "timeout": self.timeout}
        if files:
            params["files"] = files
        else:
            headers["content-type"] = "application/json"

        if data and method.lower() not in ["get", "delete"]:
            params["data"] = data

        response = request(**params)
        if response.status_code >= 400:
            raise ClientRequestError(response.content)

        return response
