import pytest


# 数组的形式
@pytest.mark.parametrize("role,word", [["胡一菲", "原谅你，那是上帝的事情，我的任务就是送你去见上帝"],
                                       ["曾小贤", "好男人就是我，我就是曾小贤"], ["陈美嘉", "我一口盐汽水喷死你"]])
def test_parametrize_02(role,word):
    print(f'{role}的台词是{word}')


# 元组的形式
@pytest.mark.parametrize("role,word", [("胡一菲", "原谅你，那是上帝的事情，我的任务就是送你去见上帝"),
                                       ("曾小贤", "好男人就是我，我就是曾小贤"), ("陈美嘉", "我一口盐汽水喷死你")])
def test_parametrize_02(role,word):
    print(f'{role}的台词是{word}')