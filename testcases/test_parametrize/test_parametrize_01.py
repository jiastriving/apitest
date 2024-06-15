import pytest


# 单参数，单次循环
@pytest.mark.parametrize("key", ["value"])
def test_parametrize(key):
    print("我是" + key)


# 单参数，多次循环
@pytest.mark.parametrize("role", ["胡一菲", "曾小贤", "陈美嘉"])
def test_parametrize(role):
    print(role)


if __name__ == "__main__":
    pytest.main()
