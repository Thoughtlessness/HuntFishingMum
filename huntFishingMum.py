# encoding:gbk

from multiprocessing import Process
import requests
import random
import socks

captchaURL = "http://hx.zzhxfudai.top/%E3%80%80.asp"
dicFilePath = r"将本地密码字典路径填在这"
proxy = {"http":"socks5://127.0.0.1:10808"}
cookies = { "ASPSESSIONIDQQBRACDD":"KFCIPMKAHPEGDDKKMHKKLPNH"}
capCode = "qveq"


def chooseAPass(dic):
    return random.choice(dic)

def genMobileNum():
    mobilePrefix = ["130","131","132","133","134","135","136","137","138","139","150","151","152","153","156","157","158","159","170","171","172","173","177","178","180","181","182","183","187","188","189"]
    mobileSubfix = str(random.randint(10000000,99999999))
    return random.choice(mobilePrefix)+mobileSubfix

def genQQmail():
    qqNum = str(random.randint(10000000,999999999))
    return qqNum+"@qq.com"

def randomDC():
    DCList = ["陆行鸟","莫古力","猫小胖"]
    return random.choice(DCList)

def randomServer():
    serverList = ["紫水栈桥","摩杜纳","幻影群岛","拉诺西亚","静语庄园","白银乡","神拳痕","白金幻象","神意之地","萌芽池","海猫茶屋"]
    return random.choice(serverList)


def hunt(pid):
    dic = open(dicFilePath,"r")
    passDic = []
    for line in dic.readlines():
        passDic.append(line.replace("\n",""))
    while True:
        try:
            httpHeader = {"Cache-Control":"max-age=0",
                          "Origin":"http://ff.zzhxfudai.top",
                          "Upgrade-Insecure-Requests":"1",
                          "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
                          "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                          "Referer":"http://ff.zzhxfudai.top/login.htm",
                          "Accept-Encoding":"gzip, deflate",
                          "Accept-Language":"zh-CN,zh;q=0.9",
                          "ContentType":"application/x-www-form-urlencoded"}


            postData = {"name":genQQmail(),
                        "pass":chooseAPass(passDic),
                        "code":capCode,
                        "face": randomServer(),
                        "zone": randomDC(),
                        "level":"幻想狂欢福袋"}
            r = requests.post(captchaURL,data=postData,cookies = cookies,headers=httpHeader,proxies=proxy)
            print r.content
            print postData
            print "hunt his mum once"
        except Exception as e:
            pass



if __name__ == '__main__':
    DEBUG = True
    if DEBUG:
        hunt(9999)
    else:
        procPool = []
        for p in range(48):
            p = Process(target=hunt,args=(p,))
            procPool.append(p)
            p.start()

