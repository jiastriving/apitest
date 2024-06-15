import requests
p={
    "shouji":"18918919441",
    "appkey":"0c818521d38759e1"
}
r=requests.post(url="http://sellshop.5istudy.online/sell/shouji/query",params=p)
print(r.status_code)
print(r.json())
print(r.text)