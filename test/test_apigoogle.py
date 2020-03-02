from models.apigoogle import ApiGoogle

def test_apigoogle_api_reading_online():
    """"""

    apigoogle = ApiGoogle()
    response1, response2 = apigoogle.api_reading("Paris")

    assert response1 == 'Paris, France'
    assert response2 == {'lat': 48.856614, 'lng': 2.3522219}

def test_apigoogle_api_reading_offline(monkeypatch):
    """"""
    result = {
        "results":
        [
            {
                "formatted_address" : "new york",
                "geometry" : {'location': {'lat': 48.85837009999999, 'lng': 2.2944813}}
                }
        ]
      }

    class MockRequests:
        """"""
        def get(self, url, params):
            """"""
            return MockResponse()

    class MockResponse:
        """"""
        def json(self):
            """"""
            return result

    monkeypatch.setattr('models.apigoogle.requests', MockRequests())

    apigoogle = ApiGoogle()
    result_adress, result_coordinate = apigoogle.api_reading('new york')

    assert result_adress == 'new york'
    assert result_coordinate == {'lat': 48.85837009999999, 'lng': 2.2944813}
