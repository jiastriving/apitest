import requests
url='https://movie.douban.com/j/search_subjects'
parmas={
    "type":"movie",
    "tag":"热门",
    "page_limit":20,
    "page_start":0
}
header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 SLBrowser/9.0.3.5211 SLBChan/111"
}
r=requests.get(url=url,params=parmas,headers=header)
print(r.status_code)
print(r.json())
print(r.text)