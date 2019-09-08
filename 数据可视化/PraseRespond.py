import requests
import re
from urllib.parse import urlencode
from requests.exceptions import RequestException
import json
import csv


def get_html(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
            }
        respond = requests.get(url, headers=headers)
        if respond.status_code == 200:
            return respond.text
        else:
            return None
    except RequestException:
        return None


def prase_html(html):
    pattern = re.compile('<script>parent.resp_once\(\'(.*?)\'.*?"host":"(.*?)".*?"ip":"(.*?)".*?"as":"(.*?)".*?'
                     '"time":"(.*?)".*?"area":"(.*?)".*?', re.S)

    items = re.findall(pattern, html)

    for item in items:
        yield {
            '跳数': item[0],
            'IP': item[2],
            '主机名': item[1],
            '地区（仅供参考）': item[5],
            'ASN（仅供参考）': item[3],
            '时间（ms）': item[4]
        }


def operateDir(item):
    Str = str(item['IP'])
    if len(item['IP'])>2:
        pattern = re.compile('.*?>(.*?)<\\\\/a>')
        ip = re.findall(pattern, Str)
        item['IP'] = ''.join(ip)

    Str = str(item['ASN（仅供参考）'])
    if len(item['ASN（仅供参考）'])>2:
        pattern = re.compile('.*?>(.*?)<\\\\/a>')
        asn = re.findall(pattern, Str)
        item['ASN（仅供参考）'] = ''.join(asn)

    item['地区（仅供参考）'] = item['地区（仅供参考）'].encode('utf-8').decode("unicode_escape")
    item['地区（仅供参考）'] = item['地区（仅供参考）'].replace('\\/', '/')

    item['时间（ms）'] = item['时间（ms）'] .replace('\\/', '/')

    return item


def write_to_file(content):
    with open('test.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False)+'\n')


def write_to_file_csv(content, flag):
    with open('respond.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        if flag == 0:
            head = list(content.keys())
            writer.writerow(head)
        info = list(content.values())
        writer.writerow(info)


def submit(ip_code, node_code, protocol_code, ip_address):
    dir = {'as': '1',
           'v': ip_code,
           'a': 'get',
           'n': '1',
           'id': node_code,
           't': protocol_code,
           'ip': ip_address}

    url = 'https://tools.ipip.net/traceroute.php?' + urlencode(dir)
    html = get_html(url)
    for item in prase_html(html):
        item = operateDir(item)


def main(code, protocol, address):
    dir = {'as': '1',
           'v': '4',
           'a': 'get',
           'n': '1',
           'id': code,
           't': protocol,
           'ip': address}

    url = 'https://tools.ipip.net/traceroute.php?' + urlencode(dir)
    html = get_html(url)
    flag = 0
    for item in prase_html(html):
        item = operateDir(item)
        write_to_file_csv(item, flag)
        flag = 1

    with open('respond.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow('\n')