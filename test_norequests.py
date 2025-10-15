import norequests as requests

def test_get():
    r = requests.get("https://httpbin.org/get")
    assert r.status_code == 200
    assert "url" in r.json()

def test_post():
    r = requests.post("https://httpbin.org/post", json={"foo": "bar"})
    assert r.status_code == 200
    data = r.json()
    assert data["json"] == {"foo": "bar"}


def test_warn_on_http():
    import warnings
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        try:
            requests.get("http://httpbin.org/get")
        except Exception:
            pass
        assert any("non-SSL" in str(wi.message) for wi in w)
