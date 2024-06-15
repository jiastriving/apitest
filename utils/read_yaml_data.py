import yaml


def get_data():
    f = open("../config/data.yaml", encoding="utf8")
    data = yaml.safe_load(f)
    return data
    # print(data)
    # print(data["role"])
    # print(data["role_two"])
    # print(data["role_three"])
    # print(data["role_list"])
