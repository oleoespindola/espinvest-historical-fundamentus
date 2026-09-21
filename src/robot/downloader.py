from io import StringIO

import requests
from bs4 import BeautifulSoup

from ..constants import FUNDAMENTUS_URL, Browser


class Downloader:

    @staticmethod
    def fundamentus() -> StringIO:
        response = requests.get(FUNDAMENTUS_URL, headers=Browser.HEADERS.value)

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table", {"id": "resultado"})

        return StringIO(str(table))
