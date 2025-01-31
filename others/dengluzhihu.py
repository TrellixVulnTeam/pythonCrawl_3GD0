import requests
try:
    import cookielib
except:
    import http.cookiejar as cookielib

import re

session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename="cookies.txt")
try:
    session.cookies.load(ignore_discard = True)
except:
    print("cookie 未能加载")

agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36"
header = {
    "HOST":"www.zhihu.com",
    "Referer":"https://www.zhihu.com",
    "User-Agent":agent
}

def is_login():
    inbox_url = "https://www.zhihu.com/question/56250357/answer/148534773"
    response = session.get(inbox_url, headers=header, allow_redirects=False)
    if response.status_code != 200:
        return False
    else:
        return True

def get_xsrf():
    response = session.get("https://www.zhihu.com",headers=header)
    response_text = response.text
    match_obj = re.match(r'.*name="_xsrf" value="(.*?)"',response_text,re.DOTALL)
    xsrf=''
    if match_obj:
        xsrf=match_obj.group(1)
        return xsrf

def get_index():
    response = session.get("https://www.zhihu.com/inbox", headers=header)
    with open ("index_page.html",'wb') as f:
        f.write(response.text.encode('utf-8'))
    print('ok')

def get_captcha():
    import time
    t = str(int(time.time()*1000))
    captcha_url = "https://www.zhihu.com/captcha.gif?r={0}&type=login".format(t)
    t = session.get(captcha_url,headers=header)
    with open("captcha.jpg",'wb') as f:
        f.write(t.content)

    from PIL import Image
    try:
        im = Image.open('captcha.jpg')
        im.show()
        im.close()
    except:
        pass
    captcha=input('输入验证码\n>')
    return captcha
def zhihu_login(account,password):
    print('手机号码登录')
    post_url = "https://www.zhihu.com/login/phone_num"
    post_data = {
        "_xsrf":get_xsrf(),
        "phone_num":account,
        "password":password,
        "captcha":get_captcha()
    }

    response_text = session.post(post_url,data=post_data,headers=header)
    session.cookies.save()

#zhihu_login("15260959391","chao123456789..")
get_index()

