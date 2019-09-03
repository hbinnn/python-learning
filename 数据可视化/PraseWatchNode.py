from requests.exceptions import RequestException
import requests
from bs4 import BeautifulSoup
import time
import json
import csv
import os
import pymysql


# 获取网页html
def get_html(url):
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
def get_node(html):
    soup = BeautifulSoup(html, 'lxml')
    for option in soup.find_all('option'):
        yield {
            'code': option.attrs['value'],
            'name': option.string
        }


def write_to_file(content, ip):
    with open('node_ipv'+str(ip)+'.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False)+'\n')


# 将输出写入csv文件
def write_to_file_csv(content, ip, flag):
    if os.path.exists('node_ipv'+str(ip)+'.csv') and flag == 0:
        os.remove('node_ipv'+str(ip)+'.csv')
    with open('node_ipv'+str(ip)+'.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        if flag == 0:
            head = list(content.keys())
            writer.writerow(head)
        info = list(content.values())
        writer.writerow(info)


# 写入数据库
def writer_into_sql(item):
    db = pymysql.connect(host='localhost', user='root', password='asd123456', port=3306, db='spiders', charset='gbk')
    cursor = db.cursor()

    for table in ['ip', 'node', 'protocol']:
        sql = 'CREATE TABLE IF NOT EXISTS ' + table + ' (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, PRIMARY KEY (id))'
        cursor.execute(sql)

    sql = 'INSERT INTO node(id, name) VALUES (%s, %s)'
    try:
        if cursor.execute(sql, tuple(item.values())):
            print('Successful')
            db.commit()
    except:
        print('Failed')
        db.rollback()

    db.close()


def main(ip):
    url = 'https://tools.ipip.net/traceroute.php?v=' + str(ip)
    html = get_html(url)
    flag = 0
    for item in get_node(html):
        # write_to_file_csv(item, ip, flag)
        # writer_into_sql(item)
        flag = 1
        yield item


def run_main(i):
    ip = []
    node = []
    protocol = []
    items = []
    for item in main(i):
        items.append(item)

    ip.append(items.pop(0))
    ip.append(items.pop(0))

    protocol.append(items.pop(-1))
    protocol.append(items.pop(-1))

    node = items

    return ip, node, protocol
