import re
import webbrowser
import requests
Headers = {
    'referer': 'bilibili.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}
print('\n\n\n')
print('注意：此文档为下载B站视频封面','Ctrl + Z 强制退出')
A = input('是否继续？[是/否]')
L = 1
while True :
    if A == '是' :
        B = 1
        break
    elif A == '否' :
        B = 0
        break
    else :
        L = L + 1
        K = 1
        if L == 2 :
            A = input('\n请输入 “是” 或 “否”。\n是否继续？\n[是/否]')
        elif L == 5 :
            A = input('\n?????\n请输入 “是” 或 “否”。')
        elif L == 6 : 
            A = input('\n唉')
        elif L == 8 :
            A = input('\n最后一次机会')
        elif L == 10 :
            print('\n说话算话')
            B = 0
            break
            


while B == 1 :
    print('\n')
    BV = input('请输入BV号：')
    if re.findall("^BV1[a-zA-Z0-9]{2}4[1|y]1[a-zA-Z0-9]7[a-zA-Z0-9]{2}",BV) :
        Url = 'https://www.bilibili.com/video/'+ BV
        Catch = requests.get(url = Url , headers = Headers)
        Cover_url = re.findall('rel="apple-touch-icon" href="(.*?)@57w_57h_1c.png"',Catch.text)[0]
        print('\n')
        print(BV + ' 封面地址：',Cover_url)
        print('\n')
        webbrowser.open(Cover_url , new = 2 , autoraise = True) 
        C = input('是否继续？[是/否]')
        if C == '是' :
            B = 1
        else :
            
            B = 0
    else :
        print('BV 号不正确，请输入正确的 BV 号。\n')
        
print('已退出\n\n\n')