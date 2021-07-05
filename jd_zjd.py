#!/usr/bin/env python3
# -*- coding: utf-8 -*
'''
项目名称: JD-Script / jd_zjd 
Author: Curtin
功能：微信小程序-赚京豆-瓜分10亿京豆自动助力，默认给账号1助力，多账号才能玩~
Date: 2021/6/25 下午9:16
TG交流 https://t.me/topstyle996
TG频道 https://t.me/TopStyle2021
updateTime: 2021.7.1 11:22
'''

#####
#ck 优先读取【JDCookies.txt】 文件内的ck  再到 ENV的 变量 JD_COOKIE='ck1&ck2' 最后才到脚本内 cookies=ck
cookies='pt_key=AAJgzgGIADBMWpNEO0AmuudLCzuY_bhEjZaasfs52bL2f2ubsWBf6cmHwn2N7rK110Hb1vyjUDg;pt_pin=jd_5159f4a5f74ce;&pt_key=AAJgzvk0ADAYA00-uUc24QF7q_R4CtXEOS3JkBA50fN2ft2L3nIjOdD7uZiN0lZaQCOMJEXpuRI;pt_pin=jd_7f1ada974d34e;&pt_key=AAJgvxWYADDy9se3UvQu6LAH7N10Xal5zskIYL4QeIANKHqYHeIW5cHwFDpejXcm31gVGf8IL8w;pt_pin=jd_gMGFngToIIBp;pt_token=8xyyvcea;pwdt_id=jd_gMGFngToIIBp;&pt_key=AAJg0yR1ADBp6vQLiuqFKUf5r2F1CqbsmaJ0_-FRMS8CcseVIOHZXS7PIVG8fjl1OW6hriY0OuE;pt_pin=jd_CvsCAzofDHwS;pt_token=rwpq1fdr;pwdt_id=jd_CvsCAzofDHwS;&pt_key=AAJg2bVwADDyo3gyXpbQwxP8nro4s9J_77xgjOHN6u6cebAk2GkepRgLinlQe0fTR-06SbzDKcg;pt_pin=SUNRREC;pt_token=jw5dp9o1;pwdt_id=SUNRREC;&pt_key=AAJgzgC3ADAe7EUmqed6XOndrK49Irz4t09dUAy0LVynTEIUGlLMjLcqrS_SHdJrmwA2H8BAqr4;pt_pin=wdNShtksJewXYDz;&pt_key=AAJgwNR9ADBNe69tLJQ4AFbr41-kB62IGCcNJ7_CLz9PJm5FVD4A1R2GHE4uhDe6UFcZZgVZCu8;pt_pin=jd_5ebc59e9b99b0;pt_token=mbr6ilz2;pwdt_id=jd_5ebc59e9b99b0;&pt_key=AAJgxLHvADDKfD2VrgHkeLUMyqQJ_7YNq5A4NCMi3e-B58_-xmJyhotJa1_JOkwdj8gXkYgPy2s;pt_pin=jd_grrQSltcEvug;&pt_key=AAJgzf4uADChcpz9KV80yDNC-RTVwCVFOJ-2dRalZLkRwWQpsF8rGjq3i1DlWaadXxK8-oStvlI;pt_pin=jd_CpdtHRfBkDus;&pt_key=AAJg2xfGAEALcBkZcL6_tz9lurCoHkg2dSD5eVg2DIAb2LvJzI7bBiZ4TuqrwcJyBivvEgRfqRwAJLimaPnKKI706zrDXHCM;pt_pin=215637226-30464027;&pt_key=AAJgxaWwADBJi69nsyxlduf6DkZWxgwZ-ttSp4R7oNKXaFOR4Eu-Jo0qwOB0-WMQp4hjpj3VYuE;pt_pin=jd_sNTyzSiwjEEX;&pt_key=AAJgzsItADDOqDFJ3U64h9v6Gcla8Bbi7Zrck7pdoUd4kiLJcVb3VAEwRJuBw_z3q4qqlllYCzI;pt_pin=jd_6ed5d66fa798f;&pt_key=AAJgvhekADDkQzNJBASPGaJM2F4qvv1qR2yhYrG18D-gH-fHW1KsOZbbqCfQECH7TpaUmWglWWg;pt_pin=jd_lyscqwfvwilr;pt_token=583sj983;pwdt_id=jd_lyscqwfvwilr;pt_key=AAJgvhlBADBsTjf4yEO0QvYgmLgE4nNVJHXP0RXuJTXxGLb17Fb8L_KViL-oq_oCnvZ0Rs3RBwo;pt_pin=jd_YjSFFIZperAN;&'

#助力账号，填写pt_pin或用户名的值，如 zlzh = ['aaaa','xxxx','yyyy'] ,支持ENV export zlzh=['CurtinLV','xxxx','yyyy']
zlzh = ['jd_5159f4a5f74ce','jd_7f1ada974d34e','jd_gMGFngToIIBp','jd_CvsCAzofDHwS','SUNRREC','wdNShtksJewXYDz','jd_5ebc59e9b99b0','jd_grrQSltcEvug','jd_CpdtHRfBkDus','215637226-30464027','jd_sNTyzSiwjEEX','jd_6ed5d66fa798f','jd_6ed5d66fa798f','jd_lyscqwfvwilr','jd_YjSFFIZperAN']
]
#####



import os, re
try:
    import requests
except Exception as e:
    print(e, "\n缺少requests 模块，请执行命令安装：python3 -m pip install requests")
    exit(3)
from urllib.parse import unquote
import json
import time
requests.packages.urllib3.disable_warnings()
pwd = os.path.dirname(os.path.abspath(__file__)) + os.sep
t = time.time()
aNum = 0
beanCount = 0
class getJDCookie(object):
    # 适配各种平台环境ck
    def getckfile(self):
        if os.path.exists('/ql/config/env.sh'):
            print("当前环境青龙面板新版")
            return '/ql/config/env.sh'
        elif os.path.exists('/ql/config/cookie.sh'):
            print("当前环境青龙面板旧版")
            return '/ql/config/env.sh'
        elif os.path.exists('/jd/config/config.sh'):
            print("当前环境V4")
            return '/jd/config/config.sh'
        elif os.path.exists(pwd + 'JDCookies.txt'):
            return pwd + 'JDCookies.txt'
        else:
            return pwd + 'JDCookies.txt'
    # 获取cookie
    def getCookie(self):
        global cookies
        ckfile = self.getckfile()
        try:
            if os.path.exists(ckfile):
                with open(ckfile, "r", encoding="utf-8") as f:
                    cks = f.read()
                    f.close()
                if 'pt_key=' in cks and 'pt_pin=' in cks:
                    r = re.compile(r"pt_key=.*?pt_pin=.*?;", re.M | re.S | re.I)
                    cks = r.findall(cks)
                    if len(cks) > 0:
                        cookies = ''
                        for i in cks:
                            cookies += i
            else:
                with open(pwd + 'JDCookies.txt', "w", encoding="utf-8") as f:
                    cks = "#多账号换行，以下示例：（通过正则获取此文件的ck，理论上可以自定义名字标记ck，也可以随意摆放ck）\n账号1【Curtinlv】cookie1;\n账号2【TopStyle】cookie2;"
                    f.write(cks)
                    f.close()
                pass
        except Exception as e:
            print(f"【getCookie Error】{e}")

    # 检测cookie格式是否正确
    def getUserInfo(self, ck, pinName, userNum):
        url = 'https://me-api.jd.com/user_new/info/GetJDUserInfoUnion?orgFlag=JD_PinGou_New&callSource=mainorder&channel=4&isHomewhite=0&sceneval=2&sceneval=2&callback=GetJDUserInfoUnion'
        headers = {
            'Cookie': ck,
            'Accept': '*/*',
            'Connection': 'close',
            'Referer': 'https://home.m.jd.com/myJd/home.action',
            'Accept-Encoding': 'gzip, deflate, br',
            'Host': 'me-api.jd.com',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Mobile/15E148 Safari/604.1',
            'Accept-Language': 'zh-cn'
        }
        try:
            resp = requests.get(url=url, verify=False, headers=headers, timeout=60).text
            r = re.compile(r'GetJDUserInfoUnion.*?\((.*?)\)')
            result = r.findall(resp)
            userInfo = json.loads(result[0])
            nickname = userInfo['data']['userInfo']['baseInfo']['nickname']
            return ck, nickname
        except Exception:
            context = f"账号{userNum}【{pinName}】Cookie 已失效！请重新获取。"
            print(context)
            return ck, False

    def iscookie(self):
        """
        :return: cookiesList,userNameList,pinNameList
        """
        cookiesList = []
        userNameList = []
        pinNameList = []
        if 'pt_key=' in cookies and 'pt_pin=' in cookies:
            r = re.compile(r"pt_key=.*?pt_pin=.*?;", re.M | re.S | re.I)
            result = r.findall(cookies)
            if len(result) >= 1:
                print("您已配置{}个账号".format(len(result)))
                u = 1
                for i in result:
                    r = re.compile(r"pt_pin=(.*?);")
                    pinName = r.findall(i)
                    pinName = unquote(pinName[0])
                    # 获取账号名
                    ck, nickname = self.getUserInfo(i, pinName, u)
                    if nickname != False:
                        cookiesList.append(ck)
                        userNameList.append(nickname)
                        pinNameList.append(pinName)
                    else:
                        u += 1
                        continue
                    u += 1
                if len(cookiesList) > 0 and len(userNameList) > 0:
                    return cookiesList, userNameList, pinNameList
                else:
                    print("没有可用Cookie，已退出")
                    exit(3)
            else:
                print("cookie 格式错误！...本次操作已退出")
                exit(4)
        else:
            print("cookie 格式错误！...本次操作已退出")
            exit(4)



# 获取系统ENV环境参数优先使用 适合Ac、云服务等环境
# JD_COOKIE=cookie （多账号&分隔）
if "JD_COOKIE" in os.environ:
    if len(os.environ["JD_COOKIE"]) > 10:
        cookies = os.environ["JD_COOKIE"]
        print("已获取并使用Env环境 Cookie")
if "zlzh" in os.environ:
    if len(os.environ["zlzh"]) > 1:
        zlzh = os.environ["zlzh"]
        zlzh = zlzh.replace('[', '').replace(']', '').replace('\'', '').replace(' ', '').split(',')
        print("已获取并使用Env环境 zlzh:", zlzh)

getCk = getJDCookie()
getCk.getCookie()

# 开启助力任务
def starAssist(sid, headers):
    global aNum
    try:
        timestamp = int(round(t * 1000))
        url = 'https://api.m.jd.com/api?functionId=vvipclub_distributeBean_startAssist&body={%22activityIdEncrypted%22:%22' + sid + '%22,%22channel%22:%22FISSION_BEAN%22}&appid=swat_miniprogram&client=tjj_m&screen=1920*1080&osVersion=5.0.0&networkType=wifi&sdkName=orderDetail&sdkVersion=1.0.0&clientVersion=3.1.3&area=11&fromType=wxapp&timestamp=' + str(timestamp)
        requests.get(url=url, headers=headers, verify=False, timeout=30).json()
        aNum = 0
    except Exception as e:
        if aNum < 5:
            aNum += 1
            return starAssist(sid, headers)
        else:
            print("starAssist Error", e)
            exit(1)


#获取助力码
def getShareCode(headers):
    global assistStartRecordId, encPin, sid, aNum
    try:
        url = f'https://api.m.jd.com/api?functionId=distributeBeanActivityInfo&fromType=wxapp&timestamp={int(round(t * 1000))}'
        body = 'body=%7B%22paramData%22%3A%7B%22channel%22%3A%22FISSION_BEAN%22%7D%7D&appid=swat_miniprogram&client=tjj_m&screen=1920*1080&osVersion=5.0.0&networkType=wifi&sdkName=orderDetail&sdkVersion=1.0.0&clientVersion=3.1.3&area=11'
        responses = requests.post(url, headers=headers, data=body, verify=False, timeout=30).json()
        if responses['success']:
            data = responses['data']
            sid = data['id']
            encPin = data['encPin']
            try:
                assistStartRecordId = data['assistStartRecordId']
            except:
                starAssist(sid, header)
                return getShareCode(headers)
            aNum = 0
            return assistStartRecordId, encPin, sid
    except Exception as e:
        if aNum < 5:
            aNum += 1
            return getShareCode(headers)
        else:
            print("getShareCode Error", e)
            exit(2)

#设置请求头
def setHeaders(cookie):
    headers = {
        'Cookie': cookie,
        'content-type': 'application/x-www-form-urlencoded',
        'Connection': 'keep-alive',
        'Accept-Encoding': 'gzip,compress,br,deflate',
        'Referer': 'https://servicewechat.com/wxa5bf5ee667d91626/148/page-frame.html',
        'Host': 'api.m.jd.com',
        'User-Agent': 'Mozilla/5.0 (iPhone CPU iPhone OS 13_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.7(0x1800072d) NetType/WIFI Language/zh_CN'
    }

    return headers

def assist(ck, sid, eid, aid, user, name, a):
    global beanCount
    timestamp = int(round(t * 1000))
    headers = {
        'Cookie': ck + 'wxclient=gxhwx;ie_ai=1;',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'Referer': 'https://servicewechat.com/wxa5bf5ee667d91626/148/page-frame.html',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'api.m.jd.com',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.1(0x1800012a) NetType/WIFI Language/zh_CN',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-cn'
    }
    url = 'https://api.m.jd.com/api?functionId=vvipclub_distributeBean_assist&body=%7B%22activityIdEncrypted%22:%22' + sid + '%5Cn%22,%22assistStartRecordId%22:%22' + str(aid) + '%22,%22assistedPinEncrypted%22:%22' + eid + '%5Cn%22,%22channel%22:%22FISSION_BEAN%22%7D&appid=swat_miniprogram&client=tjj_m&screen=1920*1080&osVersion=5.0.0&networkType=wifi&sdkName=orderDetail&sdkVersion=1.0.0&clientVersion=3.1.3&area=1_72_4137_0&fromType=wxapp&timestamp=' + str(timestamp)
    resp = requests.get(url, headers=headers, verify=False, timeout=30).json()
    if resp['success']:
        print(f"用户{a}【{user}】助力【{name}】成功~")
        if resp['data']['assistedNum'] == 4:
            beanCount += 80
            print(f"{name}, 恭喜获得8毛京豆，以到账为准。")
            print("## 开启下一轮助力")
            starAssist(sid, header)
            getShareCode(header)
    else:
        print(f"用户{a}【{userNameList[a-1]}】没有助力次数了。")




#开始互助
def start():
    global header,cookiesList, userNameList, pinNameList
    print("微信小程序-赚京豆-瓜分助力")
    cookiesList, userNameList, pinNameList = getCk.iscookie()
    for ckname in zlzh:
        try:
            ckNum = userNameList.index(ckname)
        except Exception as e:
            try:
                ckNum = pinNameList.index(ckname)
            except:
                print("请检查助力账号名称是否正确？提示：助力名字可填pt_pin的值、也可以填用户名。")
                exit(9)

        print(f"### 开始助力账号【{userNameList[int(ckNum)]}】###")

        header = setHeaders(cookiesList[int(ckNum)])
        getShareCode(header)
        starAssist(sid, header)
        getShareCode(header)
        a = 1
        for i, name in zip(cookiesList, userNameList):
            if a == ckNum+1:
                a += 1
            else:
                assist(i, sid, encPin, assistStartRecordId, name, userNameList[int(ckNum)], a)
                a += 1
        if beanCount > 0:
            print(f'\n### 本次累计获得{beanCount}京豆')

if __name__ == '__main__':
    start()
