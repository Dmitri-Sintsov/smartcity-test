import xml.etree.ElementTree as ET
import threading
import itertools
import os
import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


def parse_sensors(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {
        'gateway_id': root.attrib['gateway_id'],
    }
    node_elem = root.find('node')
    if node_elem is None:
        raise ValueError('XML has no <node>')
    node = {
        'node_id': int(node_elem.attrib['id'])
    }
    for elem in node_elem.findall('value'):
        if elem.attrib['genre'] == 'user':
            elem_type = elem.attrib['label']
            node[elem_type] = float(elem.text)
    result['node'] = node
    return result


def post_sensors(url, data, encode_fn, headers={}):
    params = encode_fn(data).encode('utf-8')
    request = Request(
        url,
        data=params,
        headers=headers
    )
    response = urlopen(request)
    return response


class SensorThread(threading.Thread):

    url = 'https://swfdev.com/'

    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.sensors = None

    def run(self):
        self.sensors = parse_sensors(self.filename)
        try:
            post_sensors(
                self.__class__.url, self.sensors, json.dumps, {'Content-Type': 'application/json; charset=utf-8'}
            )
            post_sensors(
                self.__class__.url, self.sensors, urlencode
            )
        except (URLError, HTTPError) as e:
            print(self.filename)
            print(self.__class__.url, e)


threads = []
for i in itertools.count(start=1):
    filename = 'example{}.xml'.format(i)
    if not os.path.isfile(filename):
        break
    thread = SensorThread(filename)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print('Done')
