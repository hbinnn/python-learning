from bs4 import BeautifulSoup
import time
import json
import csv
import os
import pymysql
import requests
import re
from urllib.parse import urlencode
from requests.exceptions import RequestException


# 获取网页html
def getWatchNodeHTML(url):
    try:
        # 请求头部
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
        }

        respond = requests.get(url, headers=headers)

        # get请求正确 放回html文本
        if respond.status_code == 200:
            return respond.text
        else:
            return None
    except RequestException:
        return None


# 提取列表信息，包含IP版本（ipv4、ipv6），asn信息（地理信息与asn号），所用协议（icmp、tcp）
def praseWatchNode_ip(html):
    soup = BeautifulSoup(html, 'lxml')
    for item in soup.find_all(name='select', attrs={'name': 'v', 'class': 'form-control'}):
        for i in item.find_all(name='option'):
            yield {
                'code': i.attrs['value'],
                'name': i.string
            }


def praseWatchNode_asn_ipv4(html):
    soup = BeautifulSoup(html, 'lxml')
    for item in soup.find_all(name='select', attrs={'name': 'id', 'id': 'note', 'class': 'form-control J_nodeList'}):
        for i in item.find_all(name='option'):
            yield {
                'code': i.attrs['value'],
                'name': i.string
            }


def praseWatchNode_asn_ipv6(html):
    soup = BeautifulSoup(html, 'lxml')
    for item in soup.find_all(name='select', attrs={'name': 'id', 'id': 'note', 'class': 'form-control J_nodeList'}):
        for i in item.find_all(name='option'):
            yield {
                'code': i.attrs['value'],
                'name': i.string
            }


def praseWatchNode_protocol(html):
    soup = BeautifulSoup(html, 'lxml')
    for item in soup.find_all(name='select', attrs={'name': 't', 'class': 'form-control'}):
        for i in item.find_all(name='option'):
            yield {
                'code': i.attrs['value'],
                'name': i.string
            }


# 获取查询结果页面的html
def getRespondHTML(url):
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


# 提取查询结果
def praseRespond(html):
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


# 对提取的结果进行处理
def operateRespond(item):
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


# 将WatchNode输出写入csv文件
def writeWarchNode_to_file_csv(content, ip, flag):
    if os.path.exists('node_ipv'+str(ip)+'.csv') and flag == 0:
        os.remove('node_ipv'+str(ip)+'.csv')
    with open('node_ipv'+str(ip)+'.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        if flag == 0:
            head = list(content.keys())
            writer.writerow(head)
        info = list(content.values())
        writer.writerow(info)


# 将响应结果写入csv文件
def writeRespond_to_file_csv(filename, content, flag):
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        if flag == 0:
            head = list(content.keys())
            writer.writerow(head)
        info = list(content.values())
        writer.writerow(info)


# 获取监控点网页主函数
"""
def getWatchNode_main(ip):
    url = 'https://tools.ipip.net/traceroute.php?v=' + str(ip)
    html = getWatchNodeHTML(url)
    flag = 0
    for item in praseWatchNode_ip(html):
        writeWarchNode_to_file_csv(item, ip, flag)
        flag = 1
        yield item
"""


# 获取响应页面html函数
def getRespond_main(code, protocol, address):
    dir = {'as': '1',
           'v': '4',
           'a': 'get',
           'n': '1',
           'id': code,
           't': protocol,
           'ip': address}

    url = 'https://tools.ipip.net/traceroute.php?' + urlencode(dir)
    html = getRespondHTML(url)
    flag = 0
    for item in praseRespond(html):
        item = operateRespond(item)
        writeRespond_to_file_csv(item, flag)
        flag = 1

    with open('respond.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow('\n')


"""
# 处理响应主函数
def run_getRespond_main(i):
    ip = []
    node = []
    protocol = []
    items = []
    for item in getWatchNode_main(i):
        items.append(item)

    ip.append(items.pop(0))
    ip.append(items.pop(0))

    protocol.append(items.pop(-1))
    protocol.append(items.pop(-1))

    node = items

    return ip, node, protocol
"""