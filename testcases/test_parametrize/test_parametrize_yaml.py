from utils.read_yaml_data import get_data

import pytest
import requests


@pytest.mark.parametrize("shouji,appkey", get_data()['tel_params'])
def test_tel(shouji, appkey):
    print(shouji, appkey)
    p = {"shouji": shouji, "appkey": appkey}
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