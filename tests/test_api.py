import pytest
import os
import json
from inspire.utils import NinjaAPI


@pytest.fixture
def napi_bad_key():
    return NinjaAPI("fake_key")

@pytest.fixture
def napi():
    return NinjaAPI(api_key=os.environ.get("API_NINJAS_KEY"))

def test_bad_key(napi_bad_key):
    response = napi_bad_key._make_request()
    assert response.status_code == 400

def test_bad_category(napi):
    with pytest.raises(AssertionError):
        napi.get_quote("bad_category")

def test_request(napi):
    assert napi.api_key
    response = napi._make_request("happiness")
    assert response.status_code == 200
    data = json.loads(response.text)[0]
    assert "author" in data
    assert "quote" in data
    assert data['category'] == 'happiness'
    
    try:
        assert data['category'] == 'happines'
    except Exception as e:
        assert isinstance(e, AssertionError)