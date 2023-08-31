import os
import io

import requests
import pandas

from . import constants


class ApiException(Exception):

    def __init__(self, message: str):
        super().__init__(message)


class Client:

    def __init__(
        self,
        api_key: str = None,
        api_base_url: str = None
    ):
        if api_key is None:
            api_key = os.getenv("CRUNCHDAO_API_KEY")
        if api_key is None:
            raise ValueError(
                "missing api key, "
                "either specify it with `api_key` parameter or `CRUNCHDAO_API_KEY` environment variable"
            )

        if api_base_url is None:
            api_base_url = os.getenv("API_BASE_URL")
        if api_base_url is None:
            api_base_url = constants.API_BASE_URL

        self.api_base_url = api_base_url

        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"API-Key {api_key}"
        })

    def orthogonalize(
        self,
        y: pandas.DataFrame,
        date_column_name: str = "date"
    ):
        response = self.session.post(
            self.api_base_url + "/orthogonalize",
            files={
                "file": io.StringIO(y.to_csv(index=False))
            },
            data={
                "date_column_name": date_column_name
            }
        )

        if not response.ok:
            raise ValueError(f"failed to orthogonalize: {response.text}")

        bytes = io.BytesIO(response.content)
        return pandas.read_csv(bytes)
