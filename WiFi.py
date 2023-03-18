import requests
url='http://1.1.1.3/ac_portal/login.php'
data={
    "opr": "pwdLogin",
    "userName": "cuijie",
    "pwd": "150382",
    "auth_tag": "1662033562287",
    "rememberPwd": "0",
}
header={
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "82",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host":"1.1.1.3",
    "Origin": "http://1.1.1.3",
    "Referer": "http://1.1.1.3/ac_portal/default/pc.html?template=default&tabs=pwd&vlanid=0&_ID_=0&switch_url=&url=&controller_type=&mac=b0-45-02-bf-02-c7",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
}
response = requests.post(url, data, headers=header).status_code  # POST 方式向 URL 发送表单，同时获取状态码
print("状态码{}".format(response))

