from models.apiwiki import ApiWikipedia


def test_apiwiki_get_page_id_online():
    """"""
    apiwiki = ApiWikipedia()
    response = apiwiki.api_get_page_id(48.85837009999999, 2.2944813)

    assert response == 1359783


def test_apiwiki_get_page_id_offline(monkeypatch):
    """"""
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
        def get(self, url, params):
            return MockResponse(200)

    class MockResponse:
        def __init__(self, code):
            self.status_code = code

        def json(self):
            return result

    monkeypatch.setattr('models.apiwiki.requests', MockRequests())

    apiwiki = ApiWikipedia()
    pageid = apiwiki.api_get_page_id(48.85837009999999, 2.2944813)

    assert pageid == 5


def test_apiwiki_get_extract_online():
    """"""
    apiwiki = ApiWikipedia()
    response = apiwiki.api_get_extract(1359783)

    assert response[:14] == 'La tour Eiffel'


def test_apiwiki_get_extract_offline(monkeypatch):
    """"""
    result = {
        'query': {
            'pages': {
                '5': {
                    'extract': 'La tour Mockel'
                }
            }
        }
    }

    class MockRequests:
        """"""
        def get(self, url, params):
            """"""
            return MockResponse(200)

    class MockResponse:
        """"""
        def __init__(self, code):
            """"""
            self.status_code = code

        def json(self):
            """"""
            return result

    monkeypatch.setattr('models.apiwiki.requests', MockRequests())

    apiwiki = ApiWikipedia()
    extract = apiwiki.api_get_extract(5)

    assert extract == 'La tour Mockel'
