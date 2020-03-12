from models.apiwiki import ApiWikipedia


def test_apiwiki_get_page_id_online():
    """WikiPedia API test online id page"""

    apiwiki = ApiWikipedia()
    response = apiwiki.api_get_page_id(48.85837009999999, 2.2944813)

    assert response == 1359783


def test_apiwiki_get_page_id_offline(monkeypatch):
    """WikiPedia API test offline id page"""

    result = {
        'query': {
            'geosearch':
            [
                {
                    'pageid': 5
                }
            ]
        }
    }

    class MockRequests:
        """Mock class Requests"""

        def get(self, url, params):
            """Mock method get function"""

            return MockResponse(200)

    class MockResponse:
        """Mock class Response"""

        def __init__(self, code):
            """Wiki API code initialization"""

            self.status_code = code

        def json(self):
            """Mock method json function"""

            return result

    monkeypatch.setattr('models.apiwiki.requests', MockRequests())

    apiwiki = ApiWikipedia()
    pageid = apiwiki.api_get_page_id(48.85837009999999, 2.2944813)

    assert pageid == 5


def test_apiwiki_get_extract_online():
    """WikiPedia API test online extract"""

    apiwiki = ApiWikipedia()
    response1, response2 = apiwiki.api_get_extract(1359783)

    assert response1[:14] == 'La tour Eiffel'
    assert response2 == 'https://fr.wikipedia.org/wiki/Tour_Eiffel'


def test_apiwiki_get_extract_offline(monkeypatch):
    """WikiPedia API test offline extract"""

    result = {
        'query': {
            'pages': {
                '5': {
                    'canonicalurl':
                    'https://fr.wikipedia.org/wiki/Tour_Eiffel',
                    'extract':
                    'La tour Mockel'
                }
            }
        }
    }

    class MockRequests:
        """Mock class Requests"""

        def get(self, url, params):
            """Mock method get function"""

            return MockResponse(200)

    class MockResponse:
        """Mock class Response"""

        def __init__(self, code):
            """Wiki API code initialization"""

            self.status_code = code

        def json(self):
            """Mock method json function"""

            return result

    monkeypatch.setattr('models.apiwiki.requests', MockRequests())

    apiwiki = ApiWikipedia()
    extract_text, extract_url = apiwiki.api_get_extract(5)

    assert extract_text == 'La tour Mockel'
    assert extract_url == 'https://fr.wikipedia.org/wiki/Tour_Eiffel'
