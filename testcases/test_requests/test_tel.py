import pytest
import requests


def test_tel():
    p = {
        "shouji": "18918919441",
        "appkey": "0c818521d38759e1"
    }
    r = requests.get(url="http://sellshop.5istudy.online/sell/shouji/query", params=p)
    print(r.status_code)
    assert r.status_code == 200
    print(r.json())
    result = r.json()
    assert result['status'] == 0
    assert result['msg'] == 'ok'
    assert result['result']["shouji"] == "18918919441"
    assert result['result']["province"] == "北京"
    assert result['result']["city"] == "北京"
    assert result['result']["company"] == "中国移动"
    assert result['result']["areacode"] == "0571"


def test_tel_post():
    p = {
        "shouji": "18918919441",
        "appkey": "0c818521d38759e1"
    }
    r = requests.post(url="http://sellshop.5istudy.online/sell/shouji/query", params=p)
    print(r.status_code)
    assert r.status_code == 200
    print(r.json())
    result = r.json()
    assert result['status'] == 0
    assert result['msg'] == 'ok'
    assert result['result']["shouji"] == "18918919441"
    assert result['result']["province"] == "北京"
    assert result['result']["city"] == "北京"
    assert result['result']["company"] == "中国移动"
    assert result['result']["areacode"] == "0571"


if __name__=='__main__':
    pytest.main()
