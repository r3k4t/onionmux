import os
import sys
import socks
import requests
os.system("clear")
print ("+===================================+")
print ("|             OnionMux              |")
print ("+===================================+")
print ("| Author : Rahat Khan Tusar(rkt)    |")
print ("| Github : https://github.com/r3k4t |")
print ("+===================================+")
session=requests.session()
session.proxies={}
session.proxies['http'] = 'socks5h://localhost:9050'
session.proxies['https'] = 'socks5h://localhost:9050'
onionsite=input("Enter a onion  site :")
response=session.get(onionsite)
if  not response.headers["CONNECTION"]:                                                         
     print("Link is:inactive")
else:
     print("Link is:active")
