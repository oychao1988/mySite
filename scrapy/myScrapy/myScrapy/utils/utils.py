import re
import json


def cookie_transfer(cookie_str):
    cookie_str = '{"' + cookie_str + '"}'
    cookie_sub = re.sub(r'; ', '", "', cookie_str)
    cookie_sub = re.sub(r"=", '": "', cookie_sub)
    cookie_dict = json.loads(cookie_sub)
    return cookie_dict


if __name__ == '__main__':
    cookie = cookie_transfer(
        "user_trace_token=20181003162424-bc2e8234-c6e5-11e8-a8cf-525400f775ce; LGUID=20181003162424-bc2e8853-c6e5-11e8-a8cf-525400f775ce; index_location_city=%E6%B7%B1%E5%9C%B3; WEBTJ-ID=20181008082215-166510d9256373-0c1c9d5e3a71e-3e70055f-1049088-166510d925740e; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22166527cbe742a0-094a56f8fc244b-3e70055f-1049088-166527cbe762e7%22%2C%22%24device_id%22%3A%22166527cbe742a0-094a56f8fc244b-3e70055f-1049088-166527cbe762e7%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; X_HTTP_TOKEN=84a16a5dc6d5de3f8be58743a2b0fe71; _gid=GA1.2.1131033380.1538975278; JSESSIONID=ABAAABAAADEAAFI2AA9D579308DA2197B701A300CA7B0A0; _gat=1; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; TG-TRACK-CODE=index_navigation; _ga=GA1.2.1686656861.1538555064; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1538555064,1538555073,1538958136,1538958145; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1538996928; LGSID=20181008190843-851ccace-caea-11e8-ab74-525400f775ce; LGRID=20181008190847-8752baa5-caea-11e8-bb8c-5254005c3644; SEARCH_ID=6e2183f7dcd14244ad925499b8cc00b0")
    print(cookie)
