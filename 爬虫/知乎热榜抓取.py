import re
import requests
import json
import time
import csv
from requests.exceptions import RequestException


# 抓取一个页面的html
def get_one_page(url):
    try:
        # 模拟头部信息
        headers = {
            'Cookie': '_zap=3003da89-207e-4ac3-b2e7-05617ce22069; _xsrf=PKaX2oFUygWxVjSVEGXSMcv56WR66PNo; d_c0="AIDi3ksM' 
                      '3A-PTj67B5_BE6UXG4V6NeSLzR0=|1565245211"; capsion_ticket="2|1:0|10:1565246647|14:capsion_ticket|4' 
                      '4:ZTViZTAyNGRlMWY5NGQ1OWI3YmM2ZTkyNTdlYWY5NjQ=|274e8eb442b59ab18c99ef8e3d82367cd2df53dd736feb4479' 
                      '239920316d4320"; z_c0="2|1:0|10:1565246697|4:z_c0|92:Mi4xVzhvaEFnQUFBQUFBZ09MZVN3emNEeWNBQUFDRUFs' 
                      'Vk42VkZ6WFFBaWd2cEVBcHd0cERaendTd1RsWkktV2FFLUVR|c2226d2f0860b2efcff1f24451ac37bae0c569ae62fd796f' 
                      '5a815e6d6213cf2a"; tgw_l7_route=66cb16bc7f45da64562a077714739c11; tst=h; tshl=',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.' 
                          '3729.108 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None

    except RequestException:
        return None


# 在抓取的html中提取需要的信息
def parse_one_page(html):
    pattern = re.compile('HotItem-index">.*?>(.*?)</div>.*?href="(.*?)".*?"HotItem-title">(.*?)</h2>.*?</svg>(.*?)<span', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {'index': item[0],
               'address': item[1],
               'title': item[2],
               'heat': item[3],
        }


# 将输出写入txt文件
def write_to_file(content):
    with open('知乎热榜.txt', 'a', encoding='utf-8') as f:
        localtime = time.asctime(time.localtime(time.time()))
        f.write(localtime)
        # print(type(json.dumps(content)))
        f.write(json.dumps(content, ensure_ascii=False)+'\n')


# 将输出写入csv文件
def write_to_file_csv(content, flag):
    with open('知乎热榜.csv', 'a', newline='') as csvfile:
        localtime = time.asctime(time.localtime(time.time()))
        writer = csv.writer(csvfile, delimiter=',')
        if flag == 0:
            head = list(content.keys())
            head.insert(0, 'time')
            writer.writerow(head)

        info = list(content.values())
        info.insert(0, str(localtime))
        writer.writerow(info)


def main():
    url = 'https://www.zhihu.com/hot'
    html = get_one_page(url)
    # flag标识避免多次写入csv标题
    flag = 0
    for item in parse_one_page(html):
        write_to_file_csv(item, flag)
        flag = 1


main()