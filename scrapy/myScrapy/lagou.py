import requests


def lagou():
    headers = {"Accept": "application/json,text/javascript, */*;q=0.01",
               "Accept-Encoding": "gzip, deflate",
               "Accept-Language": "zh-CN,zh;q=0.8",
               "Connection": "keep-alive",
               "Content-Length": "25",
               "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
               "Host": "www.lagou.com",
               "Origin": "https://www.lagou.com",
               "Referer": "https://www.lagou.com/jobs/list_Python?city=%E6%B7%B1%E5%9C%B3&cl=false&fromSearch=true&labelWords=&suginput=",
               "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
               "X-Anit-Forge-Code": "0",
               "X-Anit-Forge-Token": "None",
               "X-Requested-With": "XMLHttpRequest"}

    url = 'https://www.lagou.com/jobs/positionAjax.json'
    query_params = {"city": "深圳",
                    "needAddtionalResult": "false"}
    form_datas = {"first": "true",
                  "pn": "1",
                  "kd": "人工智能"}

    response = requests.post(url, headers=headers, params=query_params, data=form_datas)
    print(response.text)

