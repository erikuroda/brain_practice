import sys
import urllib.request

url = 'https://openneuro.org/crn/datasets/ds000255/snapshots/41a0d490708bb75566133bb66e2c7cf7223eb612/files/T1w.json'
urllib.request.urlretrieve(url, './T1w.json')
print('commit!')
