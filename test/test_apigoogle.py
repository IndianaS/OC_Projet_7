from models.apigoogle import ApiGoogle

import urllib.request
from io import BytesIO
import json

def test_apigoogle_api_reading(monkeypatch):
    params = {
            "address": "Rue de Rivoli, 75001 Paris, France"
        }

    class MockResponse:

        def read(self):
            results_string = json.dumps(params)
            results_bytes = results_string.encode()
            return results_bytes

    def mock_urlopen(url):
        return MockResponse()

    monkeypatch.setattr('models.apigoogle', mock_urlopen)
