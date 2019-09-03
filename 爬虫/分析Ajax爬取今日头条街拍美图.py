import requests
from urllib.parse import urlencode
import os
import time
from hashlib import md5


def get_page(offset):
    params = {
        'aid': '24' ,
        'app_name': 'web_search',
        'offset': str(offset),
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis',
        'timestamp': str(int(time.time()*1000))
    }
    headers = {

        'User-Agent': 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/74.0.3729.108 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'cookie': 'tt_webid=6727898655200544259; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6727898655200544259; csrftok'
                  'en=44afad317083b9598a6b136b7197707d; s_v_web_id=02351d2e10c6713aa3b8cc12a60f04d3; odin_tt=f64ef48241'
                  'e0a029e14733d5ecc2cdbead42b60b2bccc26e4130042955d26f7af96c8edce6e40309242ff1da83297b2172efaf6b9ecfd3'
                  '684255cadab4e07b69; passport_auth_status=8ea5a839e465eda98304e969dc1f5d80; sso_auth_status=d663c7003'
                  '94e263327f84cdae28de7e7; sso_uid_tt=29800f9b457952acf781ac3057023c12; toutiao_sso_user=6c7347840d35f'
                  'f3c020e6a1c6ea4c3f2; login_flag=9e1ee0f1d3a3aff9b24bb877a7554f1e; sessionid=8a7664e782bf8abe24003b63'
                  '9059ef95; uid_tt=172c16be77c40d6d82fe10f74bf35a9f4aceff259c17e6f229e3e7e4f3532267; sid_tt=8a7664e782'
                  'bf8abe24003b639059ef95; sid_guard="8a7664e782bf8abe24003b639059ef95|1566466373|15552000|Tue\054 18-F'
                  'eb-2020 09:32:53 GMT"; __tasessionId=dfe0f5vy21566525131760'
    }

    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None


def get_images(json):
    if json.get('data'):
        for item in json.get('data'):
            if item.get('title'):
                title = item.get('title')
                images = item.get('image_list')
                if images:
                    for image in images:
                        yield {'image': image.get('url'),
                            'title': title
                        }


def save_image(item):

    if not os.path.exists('photo\\' + item.get('title').replace('|', '').replace('"', "").replace('>', "").replace('<', "").replace(':',"")):
        os.mkdir('photo\\' + item.get('title').replace('|', '').replace('"', "").replace('>', "").replace('<', "").replace(':',""))
    try:
        response = requests.get(item.get('image'))
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format('photo\\' + item.get('title').replace('|', '').replace('"', "").replace('>', "").replace('<', "").replace(':',""), md5(response.content).hexdigest(), 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image')


def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        item['image'] = item['image'].replace('list/190x124', 'large').replace('list', 'large')
        print(item)
        save_image(item)


GROUP_START = 1
GROUP_END = 20

groups = ([(x-1) * 20 for x in range(GROUP_START, GROUP_END + 1)])
for i in groups:
    main(i)