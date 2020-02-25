from app.demo import f, g




def test_ma_fonction_f(monkeypatch):
    def mock_g():
        return "Premier test avec pytest"
    monkeypatch.setattr('app.demo.g', mock_g)
    result = f()
    assert result == "Premier test avec pytest"

def test_ma_fonction_g():
    result = g()
    assert result == "Premier test avec pytest"
