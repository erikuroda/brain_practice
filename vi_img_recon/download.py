import json
import requests
import sys
import urllib.request

#f = open('download.json', 'r')
#load_f = json.load(f)
#load_f_dict = load_f['files']
#l_urls = [d.get('urls') for d in load_f_dict]

#for i in l_urls:
#    for j in i:
#        print(j)
#        url = j

#        try:
#            r = requests.get(url)
#            print(r.text)
#        except requests.exceptions.RequestException as err:
#            print(err)

import requests
from PIL import Image
from io import BytesIO

if __name__ == '__main__':
    url = "https://www.google.co.jp/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png"
    res = requests.get(url)
    if res.status_code is 200:
        i = Image.open(BytesIO(res.content))
        i.save(f"google_logo.{i.format.lower()}")
