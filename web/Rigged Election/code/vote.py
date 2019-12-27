import requests
import hashlib
from base64 import b64encode, b64decode
from urllib3.exceptions import InsecureRequestWarning
import os
import pickle
requests.packages.urllib3.disable_warnings(category = InsecureRequestWarning)
cookies = {'PHPSESSID': 'avotdmmafadj6bsn4uc06tmkl8'}
url = 'http://challs.xmas.htsp.ro:11001/vote.php'

# dic = {}
# with open('list.txt') as f:
#     for line in f:
#         md5, ans = line.split(' ')
#         ans = int(ans)
#         dic[md5] = ans
# with open('dic.pkl', 'wb') as f:
#     pickle.dump(dic, f)

with open('dic.pkl', 'rb') as f:
    dic = pickle.load(f)

for i in range(250):
    print(i)
    while True:
        r = requests.post(f'{url}?g', cookies = cookies, verify = False)
        ans = r.text.upper()
        if ans not in dic:
            r = requests.post(f'{url}?id=16773&h=0', cookies = cookies, verify = False)
            print('jump')
            continue
        stringGen = dic[ans]
        r = requests.post(f'{url}?id=16773&h={stringGen}', cookies = cookies, verify = False)
        if 'Work confirmed' in r.text:
            print('success')
            break
        else:
            print('error')
