import requests
import re
import json
import time
import csv
from requests.exceptions import RequestException


# 抓取一个页面的html
def get_one_page(url):
    try:
        # 模拟头部信息
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko)   '
                          'Chrome/65.0.3325.162 Safari/537.36 '
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None

    except RequestException:
        return None


# 在抓取的html中提取需要的信息
def parse_one_page(html):
    # 正则表达式
    pattern = re.compile(
        '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>('
        '.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',
        re.S)
    items = re.findall(pattern, html)
    # 将得到的信息转换成字典的形式
    for item in items:
        yield {'index': item[0],
               'image': item[1],
               'title': item[2].strip(),
               'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
               'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
               'score': item[5].strip() + item[6].strip()}


# 将输出写入txt文件
def write_to_file(content):
    with open('猫眼电影榜单.txt', 'a', encoding='utf-8') as f:
        localtime = time.asctime(time.localtime(time.time()))
        f.write(localtime)
        # print(type(json.dumps(content)))
        f.write(json.dumps(content, ensure_ascii=False)+'\n')


#将输出写入csv文件
def write_to_file_csv(content, flag):
    with open('猫眼榜单.csv', 'a', newline='') as csvfile:
        localtime = time.asctime(time.localtime(time.time()))
        writer = csv.writer(csvfile, delimiter=',')
        if flag == 0:
            head = list(content.keys())
            head.insert(0, 'time')
            writer.writerow(head)

        info = list(content.values())
        info.insert(0, str(localtime))
        writer.writerow(info)


# offset为页面数
def main(offset, flag):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file_csv(item, flag)
        flag = 1


if __name__ == '__main__':
    flag = 0
    for i in range(10):
        main(i*10, flag)
        # time.sleep(1)
        flag = 1