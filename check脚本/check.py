#-*- coding:utf-8 -*-
import sys
import requests


def check(url):
    try:
        r=requests.get(url,timeout=3)
        if r.status_code==200:
            return True
        else:
            return False
    except:
        return False
    return False

def checker(ip,port):
    try:
        url="http://"+ip+":"+port
        if (check(url+"/robots.txt") and check(url)):
            return "IP: "+ip+" OK"
        else:
            return "IP: "+ip+" is down"
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    ip=sys.argv[1]
    port=sys.argv[2]
    print(checker(ip,port))
