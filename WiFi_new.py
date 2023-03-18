import requests
payload={
    "opr": "pwdLogin",
    "userName": "cuijie",
    "pwd": "a5b7345a6169",
    "auth_tag": "1678886739750",
    "rememberPwd": "0"
}
with requests.Session()as session:
    post = session.post("http://1.1.1.3/ac_portal/login.php",data=payload)
print(post)
